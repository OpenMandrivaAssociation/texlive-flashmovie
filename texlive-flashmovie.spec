# revision 25768
# category Package
# catalog-ctan /macros/latex/contrib/flashmovie
# catalog-date 2012-03-21 09:27:37 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-flashmovie
Version:	0.4
Release:	12
Summary:	Directly embed flash movies into PDF files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flashmovie
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashmovie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashmovie.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows direct embedding of flash movies into PDF
files. It is designed for use with pdflatex. The package takes
advantage of the embedded Adobe Flash player in Adobe Reader 9;
the reader is invoked with the 'rich media annotation' feature,
described in "Adobe Supplement to the ISO 32000 BaseVersion:
1.7 ExtensionLevel: 3". This method of embedding movies is
attractive since it removes all platform dependencies; however,
the user is required to use Acrobat 9.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flashmovie/flashmovie.sty
%{_texmfdistdir}/tex/latex/flashmovie/player_flv_maxi.swf
%doc %{_texmfdistdir}/doc/latex/flashmovie/README
%doc %{_texmfdistdir}/doc/latex/flashmovie/flv-player-license/MPL-1.1
%doc %{_texmfdistdir}/doc/latex/flashmovie/flv-player-license/license.txt
%doc %{_texmfdistdir}/doc/latex/flashmovie/test-beamer-0.pdf
%doc %{_texmfdistdir}/doc/latex/flashmovie/test-beamer-0.tex
%doc %{_texmfdistdir}/doc/latex/flashmovie/test-beamer-1.tex
%doc %{_texmfdistdir}/doc/latex/flashmovie/test-flv.pdf
%doc %{_texmfdistdir}/doc/latex/flashmovie/test-flv.tex
%doc %{_texmfdistdir}/doc/latex/flashmovie/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-3
+ Revision: 790628
- Update to latest release.
- Update to latest release.
- Import texlive-flashmovie
- Import texlive-flashmovie

