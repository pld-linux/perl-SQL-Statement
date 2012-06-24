%define	pdir	SQL
%define	pnam	Statement
%include	/usr/lib/rpm/macros.perl
Summary:	SQL-Statement perl module
Summary(pl):	Modu� perla SQL-Statement
Name:		perl-SQL-Statement
Version:	0.1021
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQL-Statement - SQL parsing and processing engine.

%description -l pl
SQL-Statement - mechanizm przetwarzania SQL.

%prep
%setup -q -n SQL-Statement-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README doc/*.bnf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/SQL/*.pm
%{perl_sitearch}/SQL/Statement
%dir %{perl_sitearch}/auto/SQL/Statement
%{perl_sitearch}/auto/SQL/Statement/Statement.bs
%attr(755,root,root) %{perl_sitearch}/auto/SQL/Statement/Statement.so
%{_mandir}/man3/*
