%include	/usr/lib/rpm/macros.perl
Summary:	SQL-Statement perl module
Summary(pl):	Modu³ perla SQL-Statement
Name:		perl-SQL-Statement
Version:	0.1016
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/SQL/SQL-Statement-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
SQL-Statement - SQL parsing and processing engine.

%description -l pl
SQL-Statement - mechanizm przetwarzania SQL.

%prep
%setup -q -n SQL-Statement-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/SQL/Statement/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/SQL/Statement
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README doc/*.bnf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,doc/sql-92.bnf}.gz

%{perl_sitearch}/SQL/*.pm
%{perl_sitearch}/SQL/Statement

%dir %{perl_sitearch}/auto/SQL/Statement
%{perl_sitearch}/auto/SQL/Statement/.packlist
%{perl_sitearch}/auto/SQL/Statement/Statement.bs
%attr(755,root,root) %{perl_sitearch}/auto/SQL/Statement/Statement.so

%{_mandir}/man3/*
