---
layout: post
title: Setting up Tensorflow with Docker
date: 2021-12-08
category: note
tags: machine-learning, research
---

For the last five years, I've seemed to have a more-or-less annual fight with my Linux workstations over installing CUDA to keep on doing GPU-accelerated musical machine learning research with TensorFlow and Keras.

Each version of TensorFlow requires [_specific_ versions of CUDA and cuDNN](https://www.tensorflow.org/install/source#gpu). The install instructions involve either installing very [strange apt packages](https://www.tensorflow.org/install/gpu#install_cuda_with_apt) or finding and downloading binaries from NVIDIA. The whole things seems to take a day to get right. You know it's bad when you have three or four conflicting gists and Medium articles open just to try to install a library.

While it's possible to sit on one version for a long time, for some reason or another one part seems to need to be upgraded and then whole system is broken. 

Well I say: _no more_. The _suggested_ way to run TensorFlow is with a [docker container](https://www.tensorflow.org/install/docker) and that's what I'm going to do going forward.

Mostly for my own benefit I'm going to document the setup for going from a new Ubuntu system to being able to run one command to get open a Jupyter notebook server with GPU-connected TensorFlow running. I promise it's faster than installing CUDA.

## Install Nvidia Drivers

1. Install Ubuntu
2. make sure you have a (physical) Nvidia GPU in your computer
3. make sure you have installed the Nvidia GPU drivers. This is pretty much the default these days, but here's the one-liner to install proprietary drivers:

```
sudo ubuntu-drivers autoinstall
```

Once you have Nvidia drivers installed, you should be able to run the following command to list your installed GPUs:

```
nvidia-smi
```

If the table shows your GPU(s) and driver version, then you're ready.

While we're here, consider installing [`nvtop`](https://github.com/Syllo/nvtop), a convenient command line tool for tracking GPU utilisation:

```
sudo apt install nvtop
```


## Install `docker`

Installing Docker on Ubuntu is another one of those too-many-gist-and-medium-article questions.

The [current wisdom (2021)](https://stackoverflow.com/questions/45023363/what-is-docker-io-in-relation-to-docker-ce-and-docker-ee) seems to be to install `docker.io`, which is a [Debian-provided package](https://www.collabora.com/news-and-blog/blog/2018/07/04/docker-io-debian-package-back-to-life/) in contrast to those provided by [Docker Inc](https://docs.docker.com/engine/install/ubuntu/).

```
sudo apt install docker.io
```

**Issues:** Running docker containers without `sudo` is a perennial issue in Ubuntu. Here's some [context and solutions (link)](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue).

One fix I had to run was: `sudo chmod 666 /var/run/docker.sock`

You can test your docker install by running:

```
docker run hello-world
```

## Install `nvidia-docker`

We need Nvidia's [container toolkit (link)](https://github.com/NVIDIA/nvidia-docker) to run GPU-accelerated docker containers. The install instructions are [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker), but the short summary is:

```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt update
sudo apt install -y nvidia-docker2
sudo systemctl restart docker
```

(This is the only weird extra package repository required for this setup.. phew.)

You can test `nvidia-docker` by running a CUDA-enabled container and running `nvidia-smi` within it, e.g.:

```
docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

## Trying out a Tensorflow Container

Ok--we're ready to do some **deep learning** (really!)

Copying an example from [TensorFlow's documentation](https://www.tensorflow.org/install/docker), you can test your install with:

```
docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

This should take quite a while to get started as it has to download the fairly large `tensorflow:latest-gpu` container, but that only has to be done once.

<!-- ## A few example commands -->

## Setting up a command you can remember

All these arguments are going to be hard to remember. I've set up an aliased command in my `.bashrc` file to start up a Jupyter Notebook server that can see my `~/src` directory. This is the workflow I use for _most_ of my ML research with my workstation.

Add this to `~/.bashrc`:

```
alias tfjupyter="docker run --gpus all -it -p 8888:8888 -v ~/src:/tf/notebooks tensorflow/tensorflow:latest-gpu-jupyter"
```

So now to start up a Jupyter Notebook with tensorflow and GPUs ready to go I just type `tfjupyter`.

### Packages

One downside here is that the docker container's Python environment may not have every library that you want. For now, I'm planning to install extra packages inside my notebooks, e.g., something like:

```
!pip install keras-mdn-layer
```


## Future TODOs

- get this working with Jupyter Lab.
- test out `docker.io` working without `sudo`
- test out how this works with multiple users
- figure out a similar workflow for research using PyTorch (seems like its [similar to the above](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch))

