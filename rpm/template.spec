Name:           ros-hydro-sr-self-test
Version:        1.3.5
Release:        1%{?dist}
Summary:        ROS sr_self_test package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/sr_self_test
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-roscpp
Requires:       ros-hydro-self-test
Requires:       ros-hydro-sr-hand
Requires:       ros-hydro-sr-movements
Requires:       ros-hydro-sr-robot-msgs
BuildRequires:  gnuplot
BuildRequires:  gtest-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-self-test
BuildRequires:  ros-hydro-sr-hand
BuildRequires:  ros-hydro-sr-movements
BuildRequires:  ros-hydro-sr-robot-msgs

%description
sr_self_test

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 22 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.5-1
- Autogenerated by Bloom

* Mon Sep 22 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.5-0
- Autogenerated by Bloom

* Fri Sep 19 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.4-0
- Autogenerated by Bloom

