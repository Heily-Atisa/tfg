const List<Map<String, String>> chatMessage = [  // Datos que creo que recibiré de la api.

  /*{                         //Datos usuario
    "id": "4444",
    "username": "jorge.atisa",
    "email": "jorge.varela@atisa.es",
    "password_hash": "jhae626VVJ_.", // Regular cuándo se tienen los datosm y a cuáles accede el Chatbot.
    "created_at": "2025-01-04 09:53:45",
    "updated_at": "null",
    "is_admin": "false",
  },*/


  {               // El primer mensaje no se genera por el Chatbot para no gastar tokens, pero sí se registra en BBDD para saber quiénes acceden.
    "id": "0",
    "id_user": "0",
    "username": "",
    "id_chat": "1",
    "question": "",
    "answer": "Hola! Soy el asistente virtual de Atisa. ¿Que quieres saber?",
    "name_chat": "Nuevo chat",
    "documents_referenced": "",
    "tokens_used": "0",
    //sentiment VARCHAR(50), -- Nuevo: análisis de sentimiento de la pregunta
    "created_at": "2025-24-04 09:53:45",
  },


  {
    "id": "1",
    "id_user": "4444",
    "username": "jorge.atisa",
    "id_chat": "1",
    "question": "Como me llamo?",
    "answer": "Te llamas Jorge",
    "name_chat": "Consulta de nombre",
    "documents_referenced": "documents/dniJorge.png",
    "tokens_used": "4",
    //sentiment VARCHAR(50), -- Nuevo: análisis de sentimiento de la pregunta
    "created_at": "2025-24-04 09:54:21",
  },


  {
    "id": "2",
    "id_user": "4444",
    "username": "jorge.atisa",
    "id_chat": "1",
    "question": "Escribe un Lorem Ipsum",
    "answer": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia libero id felis tristique, non tincidunt arcu tempor. Sed vitae nisl vel ante volutpat consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia libero id felis tristique, non tincidunt arcu tempor. Sed vitae nisl vel ante volutpat consequat. Phasellus sed magna at ante tincidunt aliquet. Nullam sit amet lectus quis eros tristique volutpat. Aenean interdum felis ut arcu iaculis, vel dignissim libero facilisis. Aliquam erat volutpat. Sed ullamcorper, enim non facilisis posuere, odio purus luctus purus, at accumsan ante leo vel nisl.",
    "name_chat": "Consulta de datos personales",
    "documents_referenced": "documents/dniJorge.png",
    "tokens_used": "5",
    //sentiment VARCHAR(50), -- Nuevo: análisis de sentimiento de la pregunta
    "created_at": "2025-24-04 09:54:47",
  },

];