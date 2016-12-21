Name:           ros-indigo-turtlebot-exploration-3d
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS turtlebot_exploration_3d package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/turtlebot_exploration_3d
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-turtlebot-navigation
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-octomap-msgs
BuildRequires:  ros-indigo-octomap-ros
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
Autonomous Exploration package for a Turtulebot equiped with RGBD Sensor(Kinect,
Xtion)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 21 2016 Bona <baishi.bona@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Tue Dec 20 2016 Bona <baishi.bona@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Tue Dec 20 2016 Bona <baishi.bona@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

