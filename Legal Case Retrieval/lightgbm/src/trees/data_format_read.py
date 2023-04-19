"""

Various utilities for converting data from/to Microsoft's LETOR format.

"""

import numpy as np
# import sklearn.externals.six

def iter_lines(lines, has_targets=True, one_indexed=True, missing=0.0):
    """Transforms an iterator of lines to an iterator of LETOR rows.

    Each row is represented by a (x, y, qid, comment) tuple.

    Parameters
    ----------
    lines : iterable of lines
        Lines to parse.
    has_targets : bool, optional
        Whether the file contains targets. If True, will expect the first token
        of every line to be a real representing the sample's target (i.e.
        score). If False, will use -1 as a placeholder for all targets.
    one_indexed : bool, optional 特征id从1开始的转为从0开始
        Whether feature ids are one-indexed. If True, will subtract 1 from each
        feature id.
    missing : float, optional
        Placeholder to use if a feature value is not provided for a sample.

    Yields
    ------
    x : array of floats
        Feature vector of the sample.
    y : float
        Target value (score) of the sample, or -1 if no target was parsed.
    qid : object
        Query id of the sample. This is currently guaranteed to be a string.
    comment : str
        Comment accompanying the sample.

    """
    for line in lines:
        data, _, comment = line.rstrip().partition('#')
        toks = data.strip().split()
        # toks = line.rstrip()
        # toks = re.split('\s+', toks.strip())
        # print("toks: ", toks)
        # comment = "no comment"
        num_features = 0  # 统计特征个数
        x = np.repeat(missing, 8)
        y = -1.0
        if has_targets:
            y = float(toks[0].strip())  # 相关度label
            toks = toks[1:]
        # qid:1 => 1
        qid = _parse_qid_tok(toks[0].strip())

        # feature(id:value)
        for tok in toks[1:]:
            # fid, _, val = tok.strip().partition(':') # fid,_,val => featureID,:,featureValue
            fid, val = tok.split(":")  # featureID:featureValue
            fid = int(fid)
            val = float(val)
            if one_indexed:
                fid -= 1
            assert fid >= 0
            while len(x) <= fid:
                orig = len(x)
                # x=np.resize(x,(len(x) * 2))
                x.resize(len(x) * 2)
                x[orig:orig * 2] = missing
            x[fid] = val
            num_features = max(fid + 1, num_features)

        assert num_features > 0
        x.resize(num_features)

        yield (x, y, qid, comment)


def read_dataset(source, has_targets=True, one_indexed=True, missing=0.0):
    """Parses a LETOR dataset from `source`.

    Parameters
    ----------
    source : string or iterable of lines
        String, file, or other file-like object to parse.
    has_targets : bool, optional
        See `iter_lines`.
    one_indexed : bool, optional
        See `iter_lines`.
    missing : float, optional
        See `iter_lines`.

    Returns
    -------
    X : array of arrays of floats
      Feature matrix (see `iter_lines`).
    y : array of floats
        Target vector (see `iter_lines`).
    qids : array of objects
        Query id vector (see `iter_lines`).
    comments : array of strs
        Comment vector (see `iter_lines`).
    """
    # if isinstance(source, sklearn.externals.six.string_types):
        # source = source.splitlines(True)

    max_width = 0  # 某行最多特征个数
    xs, ys, qids, comments = [], [], [], []
    iter_content = iter_lines(source, has_targets=has_targets,
                              one_indexed=one_indexed, missing=missing)
    # x:特征向量; y:float 相关度值[0-4]; qid:string query id; comment: #后面内容
    for x, y, qid, comment in iter_content:
        xs.append(x)
        ys.append(y)
        qids.append(qid)
        comments.append(comment)
        max_width = max(max_width, len(x))

    assert max_width > 0
    # X.shape = [len(xs), max_width]
    X = np.ndarray((len(xs), max_width), dtype=np.float64)
    X.fill(missing)
    for i, x in enumerate(xs):
        X[i, :len(x)] = x
    ys = np.array(ys) if has_targets else None
    qids = np.array(qids)
    comments = np.array(comments)

    return (X, ys, qids, comments)


def _parse_qid_tok(tok):
    assert tok.startswith('qid:')
    return tok[4:]