{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  packages = [ pkgs.minikube pkgs.kubernetes-helm ];
}
