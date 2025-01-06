echo "Initiating DartVM installation process..."

# installing Dart programming language
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install apt-transport-https -y
sudo wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --yes --dearmor -o /etc/apt/trusted.gpg.d/dart.gpg
sudo echo 'deb [signed-by=/etc/apt/trusted.gpg.d/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install dart -y
export PATH="$PATH:/usr/lib/dart/bin"

dart --version

# # WITH --no-check-certificate
# sudo wget --no-check-certificate -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --yes --dearmor -o /usr/share/keyrings/dart.gpg
