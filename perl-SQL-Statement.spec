%include	/usr/lib/rpm/macros.perl
%define		pdir	SQL
%define		pnam	Statement
Summary:	SQL::Statement Perl module
Summary(cs):	Modul SQL::Statement pro Perl
Summary(da):	Perlmodul SQL::Statement
Summary(de):	SQL::Statement Perl Modul
Summary(es):	Módulo de Perl SQL::Statement
Summary(fr):	Module Perl SQL::Statement
Summary(it):	Modulo di Perl SQL::Statement
Summary(ja):	SQL::Statement Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	SQL::Statement ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul SQL::Statement
Summary(pl):	Modu³ Perla SQL::Statement
Summary(pt):	Módulo de Perl SQL::Statement
Summary(pt_BR):	Módulo Perl SQL::Statement
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl SQL::Statement
Summary(sv):	SQL::Statement Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl SQL::Statement
Summary(zh_CN):	SQL::Statement Perl Ä£¿é
Name:		perl-SQL-Statement
Version:	1.004
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-warning.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQL::Statement - SQL parsing and processing engine.

%description -l pl
SQL::Statement - mechanizm przetwarzania SQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/SQL
%{_mandir}/man3/*
