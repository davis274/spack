##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Er(CMakePackage):
    """Encoding and redundancy on a file set"""

    homepage = "https://github.com/ECP-VeloC/er"
    url      = "https://github.com/ECP-VeloC/er/archive/v0.0.1.zip"

    version('0.0.1', 'e0b83da2df71286d14779312e1fbadf5')

    depends_on('mpi')
    depends_on('kvtree')
    depends_on('redset')
    depends_on('shuffile')

    def cmake_args(self):
        args = []
        args.append("-DMPI_C_COMPILER=%s" % spec['mpi'].mpicc)
        if self.spec.satisfies('platform=cray'):
            args.append("-DER_LINK_STATIC=ON")
        args.append("-DWITH_KVTREE_PREFIX=%s" % spec['kvtree'].prefix)
        args.append("-DWITH_REDSET_PREFIX=%s" % spec['redset'].prefix)
        args.append("-DWITH_SHUFFILE_PREFIX=%s" % spec['shuffile'].prefix)
        return args