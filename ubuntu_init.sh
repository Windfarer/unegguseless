# install essenstials
sudo apt update
sudo apt upgrade
sudo apt install -y build-essential ca-certificates curl
sudo apt install -y zlib1g-dev libssl-dev lzma libbz2-dev libsqlite3-dev libreadline-dev libffi-dev
 
# install docker
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo groupadd docker
sudo usermod -aG docker $USER

## init nvidia stack
# get download link https://www.nvidia.com/download/driverResults.aspx/224350/en-us/
wget http://url-for/NVIDIA-Linux-x86_64-550.54.15.run

chmod +x NVIDIA-Linux-x86_64-550.54.15.run 
sudo ./NVIDIA-Linux-x86_64-550.54.15.run

curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg   && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list |     sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |     sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# # install python env
# curl https://pyenv.run | bash

# vim .bashrc

# pyenv install 3.10
# pyenv global 3.10

sudo apt-get install python3-venv

curl -sSL https://install.python-poetry.org | python3 -
