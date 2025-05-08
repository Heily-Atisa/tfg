import 'package:flutter/material.dart';
import 'package:frontend_flutter/screens/chat.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Chatbot Atisa',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color.fromARGB(255, 86, 181, 46)),
      ),
      home: const MyHomePage(title: 'Login'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(

        backgroundColor: Theme.of(context).colorScheme.inversePrimary,

        title: Text(widget.title),
      ),
      body: Center(
 
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [

            Padding(
              padding: EdgeInsets.only(top: 120.0, left: 8.0, right: 8.0),
              child: Image.asset(
                'assets/images/logoatisa.png',
                width: 200,
                height: 200,
              ),
            ),

            Padding(
              padding: const EdgeInsets.only(top: 80.0, left: 20.0, right: 20.0),
              child: TextFormField(
                decoration: InputDecoration(
                  labelText: 'Username'
                ),
              )
            ),

            Padding(
              padding: const EdgeInsets.all(20.0),
              child: TextFormField(
                //obscureText: true,  // Oculta el texto
                decoration: const InputDecoration(
                  labelText: 'Password',
                ),
              )
            ),

            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextButton(onPressed: () {
                startChat(context);
              },
              child: Text('Entrar')
              ),
            ),
          ],
        ),
      ),
    );
  }
}

void startChat(BuildContext context){
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => const Chat(),
    ),
  );
}