import 'package:flutter/material.dart';
import 'package:frontend_flutter/data/data.dart';
import 'package:frontend_flutter/main.dart';
import 'package:frontend_flutter/widgets/chatinputbox.dart';
import 'package:frontend_flutter/widgets/usermessage.dart';
import 'package:frontend_flutter/widgets/botmessage.dart';

class Chat extends StatefulWidget {
  const Chat({super.key});

  @override
  State<Chat> createState() => _ChatState();
}

class _ChatState extends State<Chat> {

  final GlobalKey<ScaffoldState> scaffoldKey = GlobalKey<ScaffoldState>();

  String titulo = 'Preguntame algo!';
  String chat_name = 'Nuevo chat';

  late String inicialNombre;
  late String nombre;
  late String pregunta;
  late String respuesta;

  late String respuesta0;
  late String pregunta2;
  late String respuesta2;

  var textTitleStyle = TextStyle(
    fontSize: 14,
    fontWeight: FontWeight.bold,
    color: const Color.fromARGB(255, 255, 255, 255),
  );

  var textContentStyle = TextStyle(
    fontSize: 10,
    fontWeight: FontWeight.normal,
    color: const Color.fromARGB(255, 255, 255, 255),
  );

  @override
  void initState() {
    super.initState();                                   // Inicializo datos de 'API ficticia' antes de cargar la app.
    nombre = chatMessage[1]['username'] ?? 'Atisa';
    inicialNombre = nombre.isNotEmpty ? nombre[0].toUpperCase() : 'A';  
    pregunta = chatMessage[1]['question'] ?? 'Pregunta';
    respuesta = chatMessage[1]['answer'] ?? 'Respuesta';

    pregunta2 = chatMessage[2]['question'] ?? 'Pregunta';
    respuesta2 = chatMessage[2]['answer'] ?? 'Respuesta';
    respuesta0 = chatMessage[0]['answer'] ?? 'Hola!';
  }

  void openDrawer() {
    scaffoldKey.currentState?.openDrawer();
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      appBar: AppBar(
        title: Text(chat_name),
        actions: [
          IconButton(
            icon: const Icon(Icons.arrow_back_rounded),
            onPressed:(){
              goBack(context);
            },
          ),
          IconButton(
            icon: const Icon(Icons.add),
            onPressed:(){},
          ),
        ]
      ),
      drawer: NavigationDrawer(
        children: [
          ListTile(
            leading: const Icon(Icons.edit_document),
            title: const Text('Nuevo chat'),
            onTap:(){},
          ),
        ],
      ),
      body: Column(
        children:[


            SizedBox( height:826, // Al chat le pongo altura fija para que el inputbox y el titulo se queden fijos.
              child: ListView( children: [  // Introduzco en una ListView los mensajes (se puede hacer scroll)

                BotMessage(nombre: 'Bot', textTitleStyle: textTitleStyle, contenido: respuesta0, textContentStyle: textContentStyle, inicialNombre: 'A'),

                UserMessage(nombre: nombre, textTitleStyle: textTitleStyle, contenido: pregunta, textContentStyle: textContentStyle, inicialNombre: inicialNombre),
                BotMessage(nombre: 'Bot', textTitleStyle: textTitleStyle, contenido: respuesta, textContentStyle: textContentStyle, inicialNombre: 'A'),

                UserMessage(nombre: nombre, textTitleStyle: textTitleStyle, contenido: pregunta2, textContentStyle: textContentStyle, inicialNombre: inicialNombre),
                BotMessage(nombre: 'Bot', textTitleStyle: textTitleStyle, contenido: respuesta2, textContentStyle: textContentStyle, inicialNombre: 'A'),


                ...List.generate(20, (index) => UserMessage(nombre: nombre, textTitleStyle: textTitleStyle, contenido: pregunta, textContentStyle: textContentStyle, inicialNombre: inicialNombre)),

              ],),
            ),

            Expanded(
              child: Container(),    // Echa todo lo de abajo hacia el tope, dejando el texfield abajo
            ),

            ChatInputBox(),
        ],
      ),
    );
  }
}

void goBack(BuildContext context) {
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => const MyApp(),
    ),
  );
}
