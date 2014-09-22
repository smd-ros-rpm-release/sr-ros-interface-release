Name:           ros-hydro-sr-utilities
Version:        1.3.5
Release:        1%{?dist}
Summary:        ROS sr_utilities package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/sr_utilities
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-sr-robot-msgs
Requires:       ros-hydro-tf
BuildRequires:  gtest-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-sr-robot-msgs
BuildRequires:  ros-hydro-tf

%description
sr_utilities contains different useful header libraries (math libraries,
etc...).

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

