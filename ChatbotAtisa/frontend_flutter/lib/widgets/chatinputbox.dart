import 'package:flutter/material.dart';


class ChatInputBox extends StatelessWidget {
  const ChatInputBox({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(8.0),
      child: TextFormField(
        decoration: InputDecoration(
          border: OutlineInputBorder(),
          labelText: 'Escribe tu pregunta',
          suffixIcon: ConstrainedBox(
            constraints: BoxConstraints(
              maxWidth: 100,
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                IconButton(
                  icon: Icon(Icons.attach_file_rounded),
                  onPressed: () {},
                ),
                IconButton(
                  icon: Icon(Icons.send_rounded),
                  onPressed: () {},
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}