---
title: "Running Jupyter notebooks on iHPC"
date: "2021-10-13"
profile: false
---

This is a reference guide for accessing the iHPC system for UTS, with a focus on running Python and Jupyter notebooks on iHPC and accessing them from the desktop browser on your local machine.
<br/><br/>

## Some Helpful References

[This](https://ihpc.research.uts.edu.au/pages/documentation_rhel77/access_and_connectivity/ssh) is the reference for the website for remote access to the HPC at UTS.

[This](https://www.blopig.com/blog/2018/03/running-jupyter-notebook-on-a-remote-server-via-ssh/) is an excellent blog on using Jupyter Notebooks remotely.
<br/><br/>

## Step 1 - Open the Tunnel to iHPC

Navigate to [this link](https://vpn.uts.edu.au/vdesk/webtop.eui?webtop=/Common/webtop_vpn&webtop_type=webtop_full)
and open **Student VPN Tunnel**. The F5 VPN App should open up in a new window - accept (yes) and the tunnel will open up.
<br/><br/>

## Step 2 - Access the iHPC (command line)

At the command line using use the following command to access the

```.bash
# Generic command
ssh username@...

# Example command for my access
ssh jwmurray@ihpc.eng.uts.edu.au
```

From here you will be asked for your password - input it as normal.
<br/><br/>

## Step 3 - Connect to a Node in iHPC

Now you will be effectively working in a remote computing environment. Use the command `
cnode
` to get a list of the nodes within iHPC.

Once you have a list of the nodes on the system you can see who is working in which node and what the usage rates are. To access a specific node you will need to have been granted access previously by the iHPC administrator. This is approved through a supervisor. The two nodes available for us to use are:

- hephaestos1
- hephaestos2

To connect to one of the nodes the following code is used:

```.bash
cnode hephaestos2 # this will give the detail of only this node
ssh hephaestos2 # this will actually connect to the node
```

You now have access to the server environment and can establish a VENV based on this remote server.

There are two commands that will help navigation on the system

```.bash
cd ~ # This will get you to your own folder (Data and Templates)
cd / # This will take you to the root directory where all Data is stored.
```

The datasets for use are in the Behavioural DS project - the following command will take you there:

```.bash
cd /projects/BehavioralDS # Data sets is the folder of interest in this one
```

You have now opened a ssh tunnel to IHPC, connected to a node and accessed the Data sets in the Behavioural DS project folder on the system.
<br/><br/>

## Step 4 - Create VENV for Python

Best practice is to create a VENV for Python for each project you run. This will enable a requirements file to be created easily for tracking the packages used in the analysis thereby making it easier for others to reproduce your work.

Create this VENV in your personal folder for ease. [This link](https://python.land/virtual-environments/virtualenv) has details on how to do this.

An example is below:

```.bash
python3 -m venv my_env # make sure to use python3 as python2 doesn't have the venv command baked into it. my_env can be whatever you want to call it. Use something unique as it will be referenced when working in jupyter notebooks.
```
<br/><br/>

## Step 5 - Create a Jupyter Notebook host

Now the VENV is created (using python 3.6.8 on iHPC) we can start the Jupyter notebook host we will access remotely. Before we can do this we need to install ipython and jupyter into the VENV we jsut created. [This blog](https://deeplearning.lipingyang.org/2017/10/14/intall-ipython-and-jupyter-in-a-virtualenv/) is a good reference for how to do it.

Once the VENV is established activate it with `source myenv/bin/activate`. Once it is active we need to install iPython and Jupyter via `pip3 install ...` into the environment we have created.

Once we have done this any new packages we need to use as part of the analysis can be loaded with `pip3 install (package name)`. Ideally keep two terminal windows open, one for updated packages as required in the remote environment and one for your local machine.
<br/><br/>

## Step 6 - Set up Remote Jupyter notebooks

You'll need to set up the notebook environment on the remote server then establish the ssh environment then start it up on your local machine. Anything you save will be on the remote server, consider where notebooks are held and how to access them in the future.

[This blog](https://www.blopig.com/blog/2018/03/running-jupyter-notebook-on-a-remote-server-via-ssh/) has the details required to make this work.

Example code is below:

```.bash
jupyter notebook --port=9000 --no-browser
```

If the port is already in use it cycles through increasing by one on the port number until it serves the notebooks. This is OK as others may have used port number.

We now have established a virtual environment for python on a remote system and are serving jupyter notebooks. We now need to access them from the desktop on our local machine.
<br/><br/>

## Step 7 - Access Jupyter Notebooks being served on the server

Now we need to open up another terminal on our machine, one that will be for use in the local environment. The following command is an example of how this can be done.

```.bash
ssh -N -f -L yyyy:localhost:xxxx jwmurray@ihpc.eng.uts.edu.au
# yyyy is the number you will use on your local machine
# xxxx is the port used to serve the notebooks remotely
```
<br/><br/>

## Step 8 - Open the notebooks and weave magic

If everything has worked to this point you now have jupyter notebooks in a virtual environment being served from the powerful computers of iHPC. We just need to open up a browser and access jupyter from the local desktop. This is done in the usual manner with `localhost:yyyy` in the browser of your web browser.

From here any work you do in the notebooks will be saved on the remote server in the folder from where you served the notebooks from.
<br/><br/>

## Step 9 - Terminate the session

Consult [this link](https://ihpc.research.uts.edu.au/pages/documentation_rhel77/access_and_connectivity/terminating) for details on how to terminate the current session.