# TODO
# - cleanups, system pkgs, system libs, what to package afterall?
# - what's the license, distributable?
# - adb can be found from eclipse-adt (adt-bundle-linux-x86_64-20140702/sdk/platform-tools)
#   in pld packaged in android-tools
# - download build tools, etc
#   http://dl.google.com/android/repository/build-tools_r22-linux.zip
#   http://dl.google.com/android/repository/tools_r24.1.2-linux.zip
#   http://dl.google.com/android/repository/platform-tools_r22-linux.zip
%include	/usr/lib/rpm/macros.java
Summary:	The Android SDK has all you need to create great apps to Android
Name:		android-sdk
Version:	24.3.3
Release:	0.4
License:	?
Group:		Development/Building
Source0:	http://dl.google.com/android/%{name}_r%{version}-linux.tgz
# Source0-md5:	a673e69ded991f4befcf798e18290d7a
NoSource:	0
URL:		http://developer.android.com/sdk/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

# disable debug packages, because of stupid debugedit errors:
# debugedit: canonicalization unexpectedly shrank by one character
%define		_enable_debug_packages	0

%description
The Android SDK provides you the API libraries and developer tools
necessary to build, test, and debug apps for Android.

This package provides the basic SDK tools for app development, without
an IDE.

%prep
%setup -qc
mv %{name}-linux/* .

%ifnarch %{ix86}
rm -r tools/lib/x86
rm -r tools/lib/monitor-x86
rm -r tools/lib/gles_mesa
rm tools/lib/lib*.so
rm -r tools/qemu/linux-x86
%endif
%ifnarch %{x8664}
rm -r tools/lib/monitor-x86_64
rm -r tools/lib/x86_64
rm -r tools/lib64
rm -r tools/qemu/linux-x86_64
rm tools/emulator64-*
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}

cp -a add-ons platforms tools $RPM_BUILD_ROOT%{_appdir}

ln -s %{_appdir}/tools/ddms $RPM_BUILD_ROOT%{_bindir}/ddms
ln -s %{_appdir}/tools/android $RPM_BUILD_ROOT%{_bindir}/android

# installer downloads files there
install -d $RPM_BUILD_ROOT%{_appdir}/temp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc SDK\ Readme.txt
%attr(755,root,root) %{_bindir}/ddms
%attr(755,root,root) %{_bindir}/android
%dir %{_appdir}
%dir %{_appdir}/add-ons
%dir %{_appdir}/tools
%dir %{_appdir}/tools/lib
%dir %{_appdir}/tools/lib/pc-bios
%dir %{_appdir}/tools/lib/emulator
%dir %{_appdir}/tools/proguard
%dir %{_appdir}/tools/proguard/lib
%dir %{_appdir}/tools/proguard/bin
%dir %{_appdir}/tools/proguard/ant
%dir %{_appdir}/tools/apps

# attrs like /tmp so user could add new files there which aren't system pkgs (yet)
%dir %attr(1777,root,root) %{_appdir}/platforms
%dir %attr(1777,root,root) %{_appdir}/temp

%{_appdir}/tools/ant
%{_appdir}/tools/lib/*.jar

%dir %{_appdir}/tools/qemu
%ifarch %{ix86}
%dir %{_appdir}/tools/lib/x86
%{_appdir}/tools/lib/monitor-x86
%{_appdir}/tools/lib/x86/swt.jar
%dir %{_appdir}/tools/lib/gles_mesa
%attr(755,root,root) %{_appdir}/tools/lib/gles_mesa/libGL.so
%attr(755,root,root) %{_appdir}/tools/lib/gles_mesa/libGL.so.1
%attr(755,root,root) %{_appdir}/tools/lib/gles_mesa/libosmesa.so
%dir %{_appdir}/tools/qemu/linux-x86
%attr(755,root,root) %{_appdir}/tools/qemu/linux-x86/qemu-system-aarch64
%attr(755,root,root) %{_appdir}/tools/qemu/linux-x86/qemu-system-mips64el
%attr(755,root,root) %{_appdir}/tools/qemu/linux-x86/qemu-system-x86_64
%endif
%ifarch %{x8664}
%dir %{_appdir}/tools/lib/x86_64
%{_appdir}/tools/lib/monitor-x86_64
%{_appdir}/tools/lib/x86_64/swt.jar
%dir %{_appdir}/tools/lib64
%dir %{_appdir}/tools/lib64/gles_mesa
%attr(755,root,root) %{_appdir}/tools/lib64/gles_mesa/libGL.so
%attr(755,root,root) %{_appdir}/tools/lib64/gles_mesa/libGL.so.1
%attr(755,root,root) %{_appdir}/tools/lib64/gles_mesa/libosmesa.so
%attr(755,root,root) %{_appdir}/tools/lib64/lib64EGL_translator.so
%attr(755,root,root) %{_appdir}/tools/lib64/lib64GLES_CM_translator.so
%attr(755,root,root) %{_appdir}/tools/lib64/lib64GLES_V2_translator.so
%attr(755,root,root) %{_appdir}/tools/lib64/lib64OpenglRender.so
%attr(755,root,root) %{_appdir}/tools/lib64/lib64emugl_test_shared_library.so
%dir %{_appdir}/tools/qemu/linux-x86_64
%attr(755,root,root) %{_appdir}/tools/qemu/linux-x86_64/qemu-system-aarch64
%attr(755,root,root) %{_appdir}/tools/qemu/linux-x86_64/qemu-system-mips64el
%attr(755,root,root) %{_appdir}/tools/qemu/linux-x86_64/qemu-system-x86_64
%endif
%{_appdir}/tools/lib/android.el
%{_appdir}/tools/lib/build.template
%{_appdir}/tools/lib/devices.xml
%{_appdir}/tools/lib/hardware-properties.ini
%{_appdir}/tools/lib/plugin.prop

%if "%{_lib}" != "lib"
%dir %{_appdir}/tools/%{_lib}
%endif
%attr(755,root,root) %{_appdir}/tools/%{_lib}/libEGL_translator.so
%attr(755,root,root) %{_appdir}/tools/%{_lib}/libGLES_CM_translator.so
%attr(755,root,root) %{_appdir}/tools/%{_lib}/libGLES_V2_translator.so
%attr(755,root,root) %{_appdir}/tools/%{_lib}/libOpenglRender.so
%attr(755,root,root) %{_appdir}/tools/%{_lib}/libemugl_test_shared_library.so

%{_appdir}/tools/lib/build_gradle.template
%{_appdir}/tools/lib/emulator/skins
%{_appdir}/tools/lib/emulator/snapshots.img
%{_appdir}/tools/lib/pc-bios/bios.bin
%{_appdir}/tools/lib/pc-bios/vgabios-cirrus.bin
%{_appdir}/tools/support
%{_appdir}/tools/templates

%{_appdir}/tools/NOTICE.txt
%{_appdir}/tools/source.properties

%{_appdir}/tools/lib/proguard-project.txt
%{_appdir}/tools/lib/uibuild.template
%{_appdir}/tools/proguard/README
%{_appdir}/tools/proguard/docs
%{_appdir}/tools/proguard/examples
%{_appdir}/tools/proguard/license.html
%{_appdir}/tools/proguard/proguard-android-optimize.txt
%{_appdir}/tools/proguard/proguard-android.txt
%{_appdir}/tools/proguard/proguard-project.txt

%attr(755,root,root) %{_appdir}/tools/android
%attr(755,root,root) %{_appdir}/tools/ddms
%attr(755,root,root) %{_appdir}/tools/draw9patch
%attr(755,root,root) %{_appdir}/tools/hierarchyviewer
%attr(755,root,root) %{_appdir}/tools/jobb
%attr(755,root,root) %{_appdir}/tools/lint
%attr(755,root,root) %{_appdir}/tools/mksdcard
%attr(755,root,root) %{_appdir}/tools/monitor
%attr(755,root,root) %{_appdir}/tools/monkeyrunner
%attr(755,root,root) %{_appdir}/tools/screenshot2
%attr(755,root,root) %{_appdir}/tools/traceview
%attr(755,root,root) %{_appdir}/tools/uiautomatorviewer

%ifarch %{ix86}
%attr(755,root,root) %{_appdir}/tools/emulator
%attr(755,root,root) %{_appdir}/tools/emulator-arm
%attr(755,root,root) %{_appdir}/tools/emulator-mips
%attr(755,root,root) %{_appdir}/tools/emulator-ranchu-arm64
%attr(755,root,root) %{_appdir}/tools/emulator-ranchu-mips64
%attr(755,root,root) %{_appdir}/tools/emulator-x86
%endif
%ifarch %{x8664}
%attr(755,root,root) %{_appdir}/tools/emulator64-arm
%attr(755,root,root) %{_appdir}/tools/emulator64-mips
%attr(755,root,root) %{_appdir}/tools/emulator64-ranchu-arm64
%attr(755,root,root) %{_appdir}/tools/emulator64-ranchu-mips64
%attr(755,root,root) %{_appdir}/tools/emulator64-x86
%endif

%attr(755,root,root) %{_appdir}/tools/proguard/bin/proguard.sh
%attr(755,root,root) %{_appdir}/tools/proguard/bin/proguardgui.sh
%attr(755,root,root) %{_appdir}/tools/proguard/bin/retrace.sh
%{_appdir}/tools/proguard/ant/task.properties
%{_appdir}/tools/proguard/lib/*.jar

%{_appdir}/tools/apps/SdkController
