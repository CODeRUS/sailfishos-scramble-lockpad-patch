Name:       sailfishos-scramble-lockpad-patch

BuildArch: noarch

Summary:    Scramble keypad buttons on devicelock
Version:    0.0.3
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager

%description
Scramble keypad buttons on devicelock


%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-scramble-lockpad-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-scramble-lockpad-patch

%pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-scramble-lockpad-patch || true
fi

%preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-scramble-lockpad-patch || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-scramble-lockpad-patch
