pkgname=memphis-traffic-analyzer
pkgver=0.0.1.r0.g6f9ed45
pkgrel=1
pkgdesc="Graphic analyzer for Memphis-V traffic"
arch=(any)
url="https://github.com/aedalzotto/memphis-traffic-analyzer"
license=(MIT)
depends=(
  python-matplotlib
  python-pandas
)
makedepends=(
  git
  python-build 
  python-installer 
  python-wheel 
)

pkgver() {
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd ..
  python -m build --wheel --no-isolation
}

package() {
  cd ..
  python -m installer --destdir="$pkgdir" dist/*.whl
}
