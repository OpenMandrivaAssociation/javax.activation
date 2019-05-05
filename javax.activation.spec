Name: javax.activation
Version: 1.2.0
Release: 3
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

%package javadoc
Summary: Javadoc documentation for javax.inject
Group: Development/Java

%description javadoc
Javadoc documentation for javax.inject

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
javadoc -d docs -sourcepath . javax.activation
cp %{S:1} .

%install
mkdir -p %{buildroot}%{_javadir} %{buildroot}%{_mavenpomdir} %{buildroot}%{_javadocdir}
cp javax.activation-%{version}.jar %{buildroot}%{_javadir}
cp *.pom %{buildroot}%{_mavenpomdir}/
%add_maven_depmap javax.activation-%{version}.pom javax.activation-%{version}.jar
cp -a docs %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}
