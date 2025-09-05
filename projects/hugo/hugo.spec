Name:           hugo
Version:        0.148.2
Release:        1%{?dist}
Summary:        The world’s fastest framework for building websites.
License:        Apache-2.0
Vendor:         Test-Only
URL:            https://gohugo.io
Source0:        source.tar.gz
BuildRequires:  go

%description
Hugo is one of the most popular open-source static site generators.
With its amazing speed and flexibility, Hugo makes building websites fun again.

%prep
%setup -q

%build
go build -ldflags="-s -w" -buildmode=pie
./hugo completion bash > hugo.bash
./hugo completion bash > hugo.zsh
./hugo completion fish > hugo.fish

%check
go test

%install
install -Dm 755 hugo %{buildroot}%{_bindir}/hugo
install -Dm 644 hugo.bash %{buildroot}%{_datadir}/bash-completion/completions/hugo
install -Dm 644 hugo.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_hugo
install -Dm 644 hugo.fish  %{buildroot}%{_datadir}/fish/vendor_completions.d/hugo.fish


%files
%{_bindir}/hugo
%{_datadir}/bash-completion/completions/hugo
%{_datadir}/zsh/site-functions/_hugo
%{_datadir}/fish/vendor_completions.d/hugo.fish

%license LICENSE
