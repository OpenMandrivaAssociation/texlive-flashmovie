Name:		texlive-flashmovie
Version:	25768
Release:	2
Summary:	Directly embed flash movies into PDF files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flashmovie
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashmovie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashmovie.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
