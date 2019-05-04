Name: javax.activation
Version: 1.2.0
Release: 2
Group: Development/Java
Summary: An implementation of the javax.activation API
Source0: https://repo1.maven.org/maven2/com/sun/activation/javax.activation/%{version}/javax.activation-%{version}-sources.jar
Source1: https://repo1.maven.org/maven2/com/sun/activation/javax.activation/%{version}/javax.activation-%{version}.pom
License: BSD
BuildRequires: jdk-current
BuildRequires: javapackages-local
BuildArch: noarch

%description
An implementation of the javax.activation API

%prep
%autosetup -p1 -c %{name}-%{version}

%build
. %{_sysconfdir}/profile.d/90java.sh
export PATH=$JAVA_HOME/bin:$PATH

cat >module-info.java <<'EOF'
module java.activation {
	exports javax.activation;

	requires java.logging;
	requires java.desktop;
}
EOF
find . -name "*.java" |xargs javac
find . -name "*.class" -o -name "*.properties" |xargs jar cf javax.activation-%{version}.jar META-INF
cp %{S:1} .

%install
mkdir -p %{buildroot}%{_javadir} %{buildroot}%{_mavenpomdir}
cp javax.activation-%{version}.jar %{buildroot}%{_javadir}
cp *.pom %{buildroot}%{_mavenpomdir}/
%add_maven_depmap javax.activation-%{version}.pom javax.activation-%{version}.jar

%files -f .mfiles
%{_javadir}/*.jar
