# Maintainer: Ariel Abreu <facekapow@outlook.com>
# Contributor: James Brink <brink.james@gmail.com>
# Contributor: X0rg

_gitname=darling
pkgbase=$_gitname-git
pkgname='darling-git'
pkgver=r3947.e1ac44fec
pkgrel=1
pkgdesc="Darwin/macOS emulation layer for Linux"
arch=('x86_64')
url="https://www.darlinghq.org"
license=('GPL3')
groups=('darling-git')
depends=('xz' 'fuse' 'libxml2' 'icu' 'openssl' 'bzip2' 'zlib' 'libsystemd'
    'wget' 'curl' 'sqlite' 'ruby' 'sed' 'libarchive' 'file' 'python' 'gawk' 'libunwind' 'ffmpeg')
_depends_x86_64=('lib32-clang' 'lib32-bzip2' 'lib32-systemd' 'lib32-libxslt' 'libpng' 'cairo' 'libtiff' 'glu' 'libbsd' 'python2')
makedepends=('git' 'cmake' 'clang' 'dkms' 'bison' 'flex' 'binutils>=2.28' 'libpng' 'cairo' 'libtiff' 'glu' 'libbsd' 'python2' 'ffmpeg' 'git-lfs')
_make_depends_x86_64=('gcc-multilib')
conflicts=('darling')
provides=('darling')

# Darling git repo and all submodules.
source=('darling-libressl-2.2.9'::'git+https://github.com/darlinghq/darling-libressl.git#branch=v2.2.9'
        'darling-libressl-2.5.5'::'git+https://github.com/darlinghq/darling-libressl.git#branch=v2.5.5'
        'darling-libressl-2.6.5'::'git+https://github.com/darlinghq/darling-libressl.git#branch=v2.6.5'
        'darling-libressl-2.8.3'::'git+https://github.com/darlinghq/darling-libressl.git#branch=v2.8.3'
        'git+https://github.com/darlinghq/cctools-port.git'
        'git+https://github.com/darlinghq/darling-adv_cmds.git'
        'git+https://github.com/darlinghq/darling-apr.git'
        'git+https://github.com/darlinghq/darling-AvailabilityVersions'
        'git+https://github.com/darlinghq/darling-awk.git'
        'git+https://github.com/darlinghq/darling-bash.git'
        'git+https://github.com/darlinghq/darling-basic_cmds.git'
        'git+https://github.com/darlinghq/darling-bc.git'
        'git+https://github.com/darlinghq/darling-BerkeleyDB.git'
        'git+https://github.com/darlinghq/darling-bind9.git'
        'git+https://github.com/darlinghq/darling-bmalloc.git'
        'git+https://github.com/darlinghq/darling-bsm.git'
        'git+https://github.com/darlinghq/darling-bzip2.git'
        'git+https://github.com/darlinghq/darling-cctools.git'
        'git+https://github.com/darlinghq/darling-cfnetwork.git'
        'git+https://github.com/darlinghq/darling-cocotron.git'
        'git+https://github.com/darlinghq/darling-commoncrypto.git'
        'git+https://github.com/darlinghq/darling-compiler-rt.git'
        'git+https://github.com/darlinghq/darling-configd.git'
        'git+https://github.com/darlinghq/darling-corecrypto.git'
        'git+https://github.com/darlinghq/darling-corefoundation.git'
        'git+https://github.com/darlinghq/darling-coretls.git'
        'git+https://github.com/darlinghq/darling-crontabs.git'
        'git+https://github.com/darlinghq/darling-csu.git'
        'git+https://github.com/darlinghq/darling-cups.git'
        'git+https://github.com/darlinghq/darling-curl.git'
        'git+https://github.com/darlinghq/darling-dbuskit.git'
        'git+https://github.com/darlinghq/darling-DirectoryService.git'
        'git+https://github.com/darlinghq/darling-dmg.git'
        'git+https://github.com/darlinghq/darling-doc_cmds.git'
        'git+https://github.com/darlinghq/darling-DSTools.git'
        'git+https://github.com/darlinghq/darling-dtrace.git'
        'git+https://github.com/darlinghq/darling-dyld.git'
        'git+https://github.com/darlinghq/darling-energytrace.git'
        'git+https://github.com/darlinghq/darling-expat.git'
        'git+https://github.com/darlinghq/darling-file_cmds.git'
        'git+https://github.com/darlinghq/darling-file.git'
        'git+https://github.com/darlinghq/darling-files.git'
        'git+https://github.com/darlinghq/darling-foundation.git'
        'git+https://github.com/darlinghq/darling.git'
        'git+https://github.com/darlinghq/darling-glut.git'
        'git+https://github.com/darlinghq/darling-gnudiff.git'
        'git+https://github.com/darlinghq/darling-gnutar.git'
        'git+https://github.com/darlinghq/darling-gpatch.git'
        'git+https://github.com/darlinghq/darling-grep.git'
        'git+https://github.com/darlinghq/darling-groff.git'
        'git+https://github.com/darlinghq/darling-Heimdal.git'
        'git+https://github.com/darlinghq/darling-icu.git'
        'git+https://github.com/darlinghq/darling-installer.git'
        'git+https://github.com/darlinghq/darling-IOGraphics.git'
        'git+https://github.com/darlinghq/darling-IOHIDFamily.git'
        'git+https://github.com/darlinghq/darling-iokitd.git'
        'git+https://github.com/darlinghq/darling-IOKitTools.git'
        'git+https://github.com/darlinghq/darling-iokituser.git'
        'git+https://github.com/darlinghq/darling-IONetworkingFamily.git'
        'git+https://github.com/darlinghq/darling-iostoragefamily.git'
        'git+https://github.com/darlinghq/darling-JavaScriptCore.git'
        'git+https://github.com/darlinghq/darling-less.git'
        'git+https://github.com/darlinghq/darling-libarchive.git'
        'git+https://github.com/darlinghq/darling-libauto.git'
        'git+https://github.com/darlinghq/darling-Libc.git'
        'git+https://github.com/darlinghq/darling-libclosure.git'
        'git+https://github.com/darlinghq/darling-libcxxabi.git'
        'git+https://github.com/darlinghq/darling-libcxx.git'
        'git+https://github.com/darlinghq/darling-libdispatch.git'
        'git+https://github.com/darlinghq/darling-libffi.git'
        'git+https://github.com/darlinghq/darling-Libinfo.git'
        'git+https://github.com/darlinghq/darling-libkqueue.git'
        'git+https://github.com/darlinghq/darling-liblzma.git'
        'git+https://github.com/darlinghq/darling-libmalloc.git'
        'git+https://github.com/darlinghq/darling-libnetwork.git'
        'git+https://github.com/darlinghq/darling-Libnotify.git'
        'git+https://github.com/darlinghq/darling-libplatform.git'
        'git+https://github.com/darlinghq/darling-libpthread.git'
        'git+https://github.com/darlinghq/darling-librpcsvc.git'
        'git+https://github.com/darlinghq/darling-Libsystem.git'
        'git+https://github.com/darlinghq/darling-libtelnet.git'
        'git+https://github.com/darlinghq/darling-libtrace.git'
        'git+https://github.com/darlinghq/darling-libxml2.git'
        'git+https://github.com/darlinghq/darling-libxpc.git'
        'git+https://github.com/darlinghq/darling-libxslt.git'
        'git+https://github.com/darlinghq/darling-mail_cmds.git'
        'git+https://github.com/darlinghq/darling-man.git'
        'git+https://github.com/darlinghq/darling-mDNSResponder.git'
        'git+https://github.com/darlinghq/darling-misc_cmds.git'
        'git+https://github.com/darlinghq/darling-MITKerberosShim.git'
        'git+https://github.com/darlinghq/darling-nano.git'
        'git+https://github.com/darlinghq/darling-network_cmds.git'
        'git+https://github.com/darlinghq/darling-newlkm.git'
        'git+https://github.com/darlinghq/darling-nghttp2.git'
        'git+https://github.com/darlinghq/darling-objc4.git'
        'git+https://github.com/darlinghq/darling-openal.git'
        'git+https://github.com/darlinghq/darling-opendirectory.git'
        'git+https://github.com/darlinghq/darling-openjdk.git'
        'git+https://github.com/darlinghq/darling-OpenLDAP.git'
        'git+https://github.com/darlinghq/darling-openpam.git'
        'git+https://github.com/darlinghq/darling-openssh.git'
        'git+https://github.com/darlinghq/darling-openssl_certificates.git'
        'git+https://github.com/darlinghq/darling-openssl.git'
        'git+https://github.com/darlinghq/darling-pam_modules.git'
        'git+https://github.com/darlinghq/darling-passwordserver_sasl.git'
        'git+https://github.com/darlinghq/darling-patch_cmds.git'
        'git+https://github.com/darlinghq/darling-pcre.git'
        'git+https://github.com/darlinghq/darling-perl.git'
        'git+https://github.com/darlinghq/darling-pyobjc.git'
        'git+https://github.com/darlinghq/darling-python.git'
        'git+https://github.com/darlinghq/darling-python_modules.git'
        'git+https://github.com/darlinghq/darling-remote_cmds.git'
        'git+https://github.com/darlinghq/darling-rsync.git'
        'git+https://github.com/darlinghq/darling-ruby.git'
        'git+https://github.com/darlinghq/darling-screen.git'
        'git+https://github.com/darlinghq/darling-security.git'
        'git+https://github.com/darlinghq/darling-SecurityTokend.git'
        'git+https://github.com/darlinghq/darlingserver.git'
        'git+https://github.com/darlinghq/darling-shell_cmds.git'
        'git+https://github.com/darlinghq/darling-SmartCardServices.git'
        'git+https://github.com/darlinghq/darling-sqlite.git'
        'git+https://github.com/darlinghq/darling-swift.git'
        'git+https://github.com/darlinghq/darling-syslog.git'
        'git+https://github.com/darlinghq/darling-system_cmds.git'
        'git+https://github.com/darlinghq/darling-tcsh.git'
        'git+https://github.com/darlinghq/darling-text_cmds.git'
        'git+https://github.com/darlinghq/darling-TextEdit.git'
        'git+https://github.com/darlinghq/darling-top.git'
        'git+https://github.com/darlinghq/darling-usertemplate.git'
        'git+https://github.com/darlinghq/darling-vim.git'
        'git+https://github.com/darlinghq/darling-WebCore.git'
        'git+https://github.com/darlinghq/darling-WTF.git'
        'git+https://github.com/darlinghq/darling-zip.git'
        'git+https://github.com/darlinghq/darling-zlib.git'
        'git+https://github.com/darlinghq/darling-zsh.git'
        'git+https://github.com/darlinghq/fmdb.git'
        'git+https://github.com/darlinghq/lzfse.git'
        'git+https://github.com/darlinghq/xcbuild.git')

# We skip md5 on all git repos
md5sums=( 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
          'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP')
options=('!buildflags')

pkgver() {
    cd "$srcdir/$_gitname"

    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    rm -rf "$srcdir/$_gitname"
    cd "$srcdir/"
    git clone --recursive https://github.com/darlinghq/darling.git
    cd "$srcdir/$_gitname"
    mkdir -pv "build"
}

build() {
    cd "$srcdir/$_gitname/build"

    echo "Running cmake."
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr

    echo "Running make."
    make
}

package() {
    cd "$srcdir/$_gitname/build"
    make DESTDIR="$pkgdir" install
}
