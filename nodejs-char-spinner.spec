%define		pkg	char-spinner
Summary:	Put a little spinner on process.stderr, as unobtrusively as possible
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	ISC
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/char-spinner/-/%{pkg}-%{version}.tgz
# Source0-md5:	a61676ddeefc87f89f60f3160f4219bb
URL:		https://github.com/isaacs/char-spinner
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Put a little spinner on process.stderr, as unobtrusively as possible.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr spin.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
