%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rosconsole
Version:        1.13.15
Release:        1%{?dist}
Summary:        ROS rosconsole package

License:        BSD
URL:            http://www.ros.org/wiki/rosconsole
Source0:        %{name}-%{version}.tar.gz

Requires:       apr-devel
Requires:       apr-util
Requires:       boost-devel
Requires:       log4cxx-devel
Requires:       ros-noetic-cpp-common
Requires:       ros-noetic-rosbuild
Requires:       ros-noetic-rostime
BuildRequires:  apr-devel
BuildRequires:  apr-util
BuildRequires:  boost-devel
BuildRequires:  log4cxx-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cpp-common
BuildRequires:  ros-noetic-rostime
BuildRequires:  ros-noetic-rosunit

%description
ROS console output library.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Feb 12 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.15-1
- Autogenerated by Bloom

* Wed Feb 12 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.14-1
- Autogenerated by Bloom

* Tue Feb 11 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.13-1
- Autogenerated by Bloom

* Tue Feb 11 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.12-1
- Autogenerated by Bloom

