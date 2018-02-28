Name:       docker-machine
Version:    0.13.0
Release:    1%{?dist}
Summary:    Machine management for Docker
License:    ASL 2.0
URL: https://github.com/docker/machine
Source0:    https://github.com/docker/machine/archive/v%{version}.tar.gz
BuildRequires: golang golint rsync openssh-clients make git
Supplements: docker

%global debug_package %{nil}

%description
Docker Machine is a tool that lets you install Docker Engine on virtual hosts,
and manage the hosts with docker-machine commands. You can use Machine to
create Docker hosts on your local Mac or Windows box, on your company network,
in your data center, or on cloud providers like Azure, AWS, or Digital Ocean.


%prep
%setup -q -n machine-%{version}

%build
export GOPATH="$PWD"
mkdir -p $GOPATH/src/github.com/docker
ln -s $PWD $GOPATH/src/github.com/docker/machine
cd src/github.com/docker/machine
make build

%check
export GOPATH="$PWD"
cd src/github.com/docker/machine
make test GOLINT=/usr/bin/golint

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 bin/docker-machine* %{buildroot}%{_bindir}/
install -D -p -m 644 contrib/completion/bash/docker-machine.bash %{buildroot}%{_datadir}/bash-completion/completions/docker-machine.bash
install -D -p -m 644 contrib/completion/zsh/_docker-machine %{buildroot}%{_datadir}/zsh-completion/completions/_docker-machine

%clean
export GOPATH="$PWD"
cd src/github.com/docker/machine
make clean

%files
%doc README.md LICENSE
%{_bindir}/docker-machine*
%{_datadir}/bash-completion
%{_datadir}/zsh-completion

%changelog

