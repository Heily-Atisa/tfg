import  'package:flutter/material.dart';


class UserMessage extends StatelessWidget {
  const UserMessage({
    super.key,
    required this.nombre,
    required this.textTitleStyle,
    required this.contenido,
    required this.textContentStyle,
    required this.inicialNombre,
  });

  final String nombre;
  final TextStyle textTitleStyle;
  final String contenido;
  final TextStyle textContentStyle;
  final String inicialNombre;

  @override
  Widget build(BuildContext context) {
    return Align( //MENSAJE------------------------------------------------------------------------------------
      alignment: Alignment.bottomRight,
      child: 
    IntrinsicWidth( 
       child:
    Container(  
      margin: EdgeInsets.only(bottom: 10),
      //height:80,
      decoration: BoxDecoration(color:Colors.black),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
    
            Container(
              width: 200,
              //height: 400,
              decoration: BoxDecoration(
                border: Border.all(color: Colors.red, width: 1),
              ),
              child: Column(
                //mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Align(
                    alignment: Alignment.topRight,   // con Alignment(0.00, 0.00) se puede personalizar el margen tambien
                    child: Text(nombre, style: textTitleStyle),
                  ),
                  
                  Padding(padding: EdgeInsets.only(bottom: 10)),
    
                  Align(
                    child: Align(
                      alignment: Alignment.centerRight,
                      child: Text(contenido, style: textContentStyle)
                    ),
                  ),
    
                ]
              ),
            ),
    
            Container(
              padding: EdgeInsets.only(top: 18, left:18, right: 18, bottom: 18),
              decoration: BoxDecoration(
                border: Border.all(color: Colors.purple, width: 1)
              ),
              child: CircleAvatar(child: Text(inicialNombre)),
            ),
            
        ]
      ),
    ), 
    ), 
    );
  }
}

