Name:		texlive-phonenumbers
Version:	63774
Release:	2
Summary:	Typesetting telephone numbers with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phonenumbers
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonenumbers.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonenumbers.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The phonenumbers package makes it possible to typeset telephone
numbers according to different national conventions. German,
Austrian, French, British and North American phone numbers are
supported. Phone numbers from other countries are supported
rudimentarily. The user can select from various formatting
options, including the additional output of the country calling
code. The package is able to check if a phone number is valid
according to the national rules. It also allows to link phone
numbers using the hyperref package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/phonenumbers
%doc %{_texmfdistdir}/doc/latex/phonenumbers

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
