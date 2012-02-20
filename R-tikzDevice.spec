%global packname  tikzDevice
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6.2
Release:          1
Summary:          A Device for R Graphics Output in PGF/TikZ Format
Group:            Sciences/Mathematics
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-filehash 
Requires:         R-testthat R-evaluate R-stringr R-ggplot2 R-maps 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-filehash
BuildRequires:    R-testthat R-evaluate R-stringr R-ggplot2 R-maps 

%description
The TikZ device enables LaTeX-ready output from R graphics functions. This
is done by producing code that can be understood by the TikZ graphics
language. All text in a graphic output with the tikz() function will can
be typeset by LaTeX and therefore will match whatever fonts are currently
used in the document. This also means that LaTeX mathematics can be
typeset directly into labels and annotations!  Graphics produced this way
can also be annotated with custom TikZ commands.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/GIT_VERSION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tests
