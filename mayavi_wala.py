def plot3d_all(trajectories, tracks):
    """
    Plot all tracks on a single 2d slice
    :param trajectories: dictionary output of the Alyx REST query on trajectories
    :param tracks:
    :return:
    """
    from mayavi import mlab
    src = mlab.pipeline.scalar_field(brat.label)
    mlab.pipeline.iso_surface(src, contours=[0.5, ], opacity=0.3)

    pts = []
    for xyz in tracks['xyz']:
        mlapdv = brat.bc.xyz2i(xyz)
        pts.append(mlab.plot3d(mlapdv[:, 1], mlapdv[:, 0], mlapdv[:, 2], line_width=3))

    plt_trj = []
    for trj in trajectories:
        ins = atlas.Insertion.from_dict(trj, brain_atlas=brat)
        mlapdv = brat.bc.xyz2i(ins.xyz)
        plt = mlab.plot3d(mlapdv[:, 1], mlapdv[:, 0], mlapdv[:, 2],
                          line_width=3, color=(1., 0., 1.))
        plt_trj.append(plt) 
