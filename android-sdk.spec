# TODO
# - cleanups, system pkgs, system libs, what to package afterall?
%include	/usr/lib/rpm/macros.java
Summary:	The Android SDK has all you need to create great apps to Android
Name:		android-sdk
Version:	r18
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/Java
URL:		http://developer.android.com/sdk/
Source0:	http://dl.google.com/android/%{name}_%{version}-linux.tgz
# Source0-md5:	6cd716d0e04624b865ffed3c25b3485c
NoSource:	0
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

%description
The Android SDK has the tools, sample code, and docs you need to
create great apps in Android Platform.

%prep
%setup -q -n %{name}-linux

%ifnarch %{ix86}
rm -rf tools/lib/x86
%endif
%ifnarch %{x8664}
rm -rf tools/lib/x86_64
%endif


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}

cp -a add-ons platforms tools $RPM_BUILD_ROOT%{_appdir}

# installer downloads files there
install -d $RPM_BUILD_ROOT%{_appdir}/temp

ln -s %{_appdir}/tools/ddms $RPM_BUILD_ROOT%{_bindir}/ddms
ln -s %{_appdir}/tools/android $RPM_BUILD_ROOT%{_bindir}/android

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
%ifarch %{ix86}
%dir %{_appdir}/tools/lib/x86
%{_appdir}/tools/lib/x86/swt.jar
%endif
%ifarch %{x8664}
%dir %{_appdir}/tools/lib/x86_64
%{_appdir}/tools/lib/x86_64/swt.jar
%endif
%{_appdir}/tools/lib/android.el
%{_appdir}/tools/lib/build.template
%{_appdir}/tools/lib/devices.xml
%{_appdir}/tools/lib/hardware-properties.ini
%{_appdir}/tools/lib/plugin.prop
%{_appdir}/tools/lib/libEGL_translator.so
%{_appdir}/tools/lib/libGLES_CM_translator.so
%{_appdir}/tools/lib/libGLES_V2_translator.so
%{_appdir}/tools/lib/libOpenglRender.so
%{_appdir}/tools/lib/pc-bios/bios.bin
%{_appdir}/tools/lib/pc-bios/vgabios-cirrus.bin
#%{_appdir}/tools/lib/proguard.cfg
%{_appdir}/tools/lib/emulator/snapshots.img

%{_appdir}/tools/NOTICE.txt
%{_appdir}/tools/source.properties

%attr(755,root,root) %{_appdir}/tools/android
%attr(755,root,root) %{_appdir}/tools/apkbuilder
%attr(755,root,root) %{_appdir}/tools/ddms
%attr(755,root,root) %{_appdir}/tools/dmtracedump
%attr(755,root,root) %{_appdir}/tools/draw9patch
%attr(755,root,root) %{_appdir}/tools/emulator
%attr(755,root,root) %{_appdir}/tools/emulator-arm
%attr(755,root,root) %{_appdir}/tools/emulator-x86
%attr(755,root,root) %{_appdir}/tools/etc1tool
%attr(755,root,root) %{_appdir}/tools/hierarchyviewer
%attr(755,root,root) %{_appdir}/tools/hprof-conv
%attr(755,root,root) %{_appdir}/tools/lint
%attr(755,root,root) %{_appdir}/tools/mksdcard
%attr(755,root,root) %{_appdir}/tools/monkeyrunner
%attr(755,root,root) %{_appdir}/tools/sqlite3
%attr(755,root,root) %{_appdir}/tools/traceview
%attr(755,root,root) %{_appdir}/tools/zipalign
%attr(755,root,root) %{_appdir}/tools/proguard/bin/proguard.sh
%attr(755,root,root) %{_appdir}/tools/proguard/bin/proguardgui.sh
%attr(755,root,root) %{_appdir}/tools/proguard/bin/retrace.sh
%{_appdir}/tools/proguard/ant/task.properties
%{_appdir}/tools/proguard/lib/*.jar

%{_appdir}/tools/apps/SdkController
