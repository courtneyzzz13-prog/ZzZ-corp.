import 'package:flutter/material.dart';

void main() => runApp(ZzZApp());

class ZzZApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ZzZ',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final userController = TextEditingController();
  final passController = TextEditingController();
  bool _isPremium = false;

  void _login() {
    setState(() {
      _isPremium = true; // For demo; connect real API for actual status
    });
    Navigator.push(context, MaterialPageRoute(
      builder: (context) => ProfilePage(username: userController.text, isPremium: _isPremium),
    ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('ZzZ Login')),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(children: [
          TextField(controller: userController, decoration: InputDecoration(labelText: 'Username')),
          TextField(controller: passController, decoration: InputDecoration(labelText: 'Password'), obscureText: true),
          ElevatedButton(child: Text('Login/Register'), onPressed: _login),
        ]),
      ),
    );
  }
}

class ProfilePage extends StatefulWidget {
  final String username;
  final bool isPremium;
  ProfilePage({required this.username, required this.isPremium});
  @override
  State<ProfilePage> createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  String _gradient = "#ff00ff,#00ffff";
  String _bannerUrl = "";
  bool _bannerAnimated = false;
  String _selectedLanguage = 'English';
  List<String> _languages = ['English', 'Spanish', 'French', 'German'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Profile: ${widget.username}"),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.purple, Colors.cyan], // Parse _gradient for real use
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: ListView(
          children: [
            // Banner
            _bannerUrl.isNotEmpty
              ? (_bannerAnimated
                  ? Image.network(_bannerUrl) // For GIFs
                  : Image.network(_bannerUrl)
                )
              : Container(height: 100, color: Colors.grey[300], child: Center(child: Text("No Banner"))),
            // Username with Crown
            Row(
              children: [
                Text(widget.username, style: TextStyle(fontSize: 24)),
                if (widget.isPremium)
                  Padding(
                    padding: EdgeInsets.only(left: 8),
                    child: Icon(Icons.emoji_events, color: Colors.amber), // Crown
                  ),
              ],
            ),
            // Gradient Picker
            ListTile(
              title: Text("Change Gradient"),
              trailing: Icon(Icons.color_lens),
              onTap: () {
                setState(() {
                  _gradient = "#00ff00,#0000ff"; // Example, add color picker
                });
              },
            ),
            // Language Picker
            DropdownButton<String>(
              value: _selectedLanguage,
              items: _languages.map((lang) {
                return DropdownMenuItem(value: lang, child: Text(lang));
              }).toList(),
              onChanged: (newLang) {
                setState(() {
                  _selectedLanguage = newLang!;
                });
              },
            ),
            // Banner Picker (just a URL for demo)
            ListTile(
              title: Text("Set Banner URL"),
              trailing: Icon(Icons.image),
              onTap: () {
                setState(() {
                  _bannerUrl = "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif";
                  _bannerAnimated = true; // Set true for GIFs
                });
              },
            ),
            // Chat navigation
            ElevatedButton(
              child: Text("Go to Group Chat"),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(
                  builder: (context) => ChatPage(username: widget.username),
                ));
              },
            ),
          ],
        ),
      ),
    );
  }
}

class ChatPage extends StatefulWidget {
  final String username;
  ChatPage({required this.username});
  @override
  State<ChatPage> createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  final messageController = TextEditingController();
  List<String> messages = [];

  void _sendMessage() {
    if (messageController.text.trim().isEmpty) return;
    setState(() {
      messages.add("${widget.username}: ${messageController.text}");
    });
    messageController.clear();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Group Chat")),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, idx) => ListTile(title: Text(messages[idx])),
            ),
          ),
          Row(
            children: [
              Expanded(
                child: TextField(
                  controller: messageController,
                  decoration: InputDecoration(hintText: "Type message"),
                ),
              ),
              IconButton(icon: Icon(Icons.send), onPressed: _sendMessage),
            ],
          ),
        ],
      ),
    );
  }
}