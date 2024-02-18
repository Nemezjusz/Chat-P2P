# P2P Chat
The main goal of the project was to deepen the knowledge about the **P2P** network. It is a topic that truly interested us and we wanted to create something based on it. We chose a chat application, which not only turned out to be a perfect tool for experiments, but also allowed us to develop knowledge about **encryption and security**, as well as improve our skills in creating a **user interface**.

## P2P
What is peer to peer?
Peer-to-peer (P2P) is a computer communication model based on the idea of decentralization. Unlike the traditional client-server model, a P2P network allows interaction and data exchange directly between all users.

## Features
The application is used for direct communication between hosts (without using a server) in a given local network. It enables the exchange of text messages as well as file exchange, regardless of their extension or size(?). We achieve this through operations on sockets(...). The exchange of messages is additionally encrypted using the **AES block cipher in ECB mode**. The key is exchanged using the asymmetric **RSA** algorithm, which ensures protection against interception. The GUI was created using the **PyQt5** library and its included Designer tool.

![image](https://github.com/Nemezjusz/Chat-P2P/assets/50834734/1a6b0313-d7ea-42d4-91e7-968f87e4c063)

In the attached image, we can observe the established connection and a fragment of the conversation on two application instances. As we can see, the message exchange is smooth and secure. Sending, in this case an image, was also successful without any loss or errors. Additionally, on the left side, we can see information describing, among others, the connection status.

### Application user manual
Before starting, you need to download the necessary libraries using the following command:
```console
pip install -r requirements.txt
```
To run the application, navigate to the downloaded application folder using the terminal and run it with the following command:
```console
python main.py
```
To test the functionality of the application, we will need a second instance of it. Open it in the same way in a second terminal window.

After starting both instances, we are ready to proceed. Set one of the applications to the waiting mode by clicking the ***Await Connection*** button. Then, in the second window, enter the appropriate IP address and click ***Connect***. If everything goes smoothly, the **Status** should change to **Connected**. At this point, we are ready to start the conversation.
