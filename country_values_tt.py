from enum import Enum

class CountryEnterEmail(Enum):
    GERMANY = "Telefonnummer oder E-Mail-Adresse nutzen"
    POLAND = "Użyj numeru telefonu lub adresu e-mail"
    SPAIN = "Usar teléfono o correo"
    GREECE = "Χρήση τηλεφώνου ή email"
    FRANCE = "Utiliser un numéro de téléphone ou une adresse e-mail"
    ITALY = "Usa telefono o email"
    BULGARIA = "Използване на телефон или имейл"
    NETHERLANDS = "Telefoonnummer of e-mailadres gebruiken"
    SWEDEN = "Använd telefon eller e-post"
    ROMANIA = "Folosește numărul de telefon sau e-mailul"
    CZECH = "Použít telefon nebo e-mail"
    FINLAND = "Käytä puhelinnumeroa tai sähköpostiosoitetta"

class CountryUseEmail(Enum):
    GERMANY = "Mit E-Mail-Adresse registrieren"
    POLAND = "Załóż konto za pomocą adresu e-mail"
    SPAIN = "Registrarse con un correo electrónico"
    GREECE = "Εγγραφή με email"
    FRANCE = "Inscription par e-mail"
    ITALY = "Registrati con l'email"
    BULGARIA = "Регистриране чрез имейл"
    NETHERLANDS = "Registreren met e-mailadres"
    SWEDEN = "Registrera dig med e-post"
    ROMANIA = "Înregistrează-te cu e-mailul"
    CZECH = "Zaregistrovat se pomocí e-mailu"
    FINLAND = "Rekisteröidy sähköpostiosoitteella"

class CountryCodeButton(Enum):
    GERMANY = "Code senden"
    POLAND = "Wyślij kod"
    SPAIN = "Enviar código"
    GREECE = "Αποστολή κωδικού"
    FRANCE = "Envoyer le code"
    ITALY = "Invia codice"
    BULGARIA = "Изпращане на код"
    NETHERLANDS = "Code sturen"
    SWEDEN = "Skicka kod"
    ROMANIA = "Trimite codul"
    CZECH = "Poslat kód"
    FINLAND = "Lähetä koodi"


class CountryNextButton(Enum):
    GERMANY = "Weiter"
    POLAND = "Dalej"
    SPAIN = "Siguiente"
    GREECE = "Επόμενο"
    FRANCE = "Suivant"
    ITALY = "Avanti"
    BULGARIA = "Напред"
    NETHERLANDS = "Volgende"
    SWEDEN = "Nästa"
    ROMANIA = "Înainte"
    CZECH = "Další"
    FINLAND = "Seuraava"




class CountryUsernameField(Enum):
    GERMANY = "Benutzername"
    POLAND = "Nazwa użytkownika"
    SPAIN = "Nombre de usuario"
    GREECE = "Όνομα χρήστη"
    FRANCE = "Nom d'utilisateur"
    ITALY = "Nome utente"
    BULGARIA = "Username"
    NETHERLANDS = "Gebruikersnaam"
    SWEDEN = "Användarnamn"
    ROMANIA = "Nume de utilizator"
    CZECH = "Uživatelské jméno"
    FINLAND = "Käyttäjätunnus"





class CountryRegisterButton(Enum):
    GERMANY = "Registrieren"    
    POLAND = "Zarejestruj się"
    SPAIN = "Registrarse"
    GREECE = "Εγγραφή"
    FRANCE = "S'inscrire"
    ITALY = "Registrati"
    BULGARIA = "Регистриране"
    NETHERLANDS = "Registreren"
    SWEDEN = "Registrera dig"
    ROMANIA = "Înregistrează-te"
    CZECH = "Zaregistrovat se"
    FINLAND = "Rekisteröidy"




class CountryRejectCookies(Enum):
    GERMANY = "Optionale Cookies ablehnen"

class CountryLanguageSettings(Enum):
    GERMANY = [ 
        {"locale": "de-DE", "languages": ["de-DE", "de"], "accept_language": "de-DE,de;q=0.9"},
        {"locale": "de-DE", "languages": ["de-DE", "en-US", "de"], "accept_language": "de-DE,de;q=0.9,en-US;q=0.8"},
    ]
    POLAND = [
        {"locale": "pl-PL", "languages": ["pl-PL", "pl"], "accept_language": "pl-PL,pl;q=0.9"},
        {"locale": "pl-PL", "languages": ["pl-PL", "pl", "en-US"], "accept_language": "pl-PL,pl;q=0.9,en-US;q=0.8"},
    ]
    SPAIN = [
        {"locale": "es-ES", "languages": ["es-ES", "es"], "accept_language": "es-ES,es;q=0.9"},
        {"locale": "es-ES", "languages": ["es-ES", "en-US", "es"], "accept_language": "es-ES,es;q=0.9,en-US;q=0.8"}
    ]
    GREECE = [
        {"locale": "el-GR", "languages": ["el-GR", "el"], "accept_language": "el-GR,el;q=0.9"},
        {"locale": "el-GR", "languages": ["el-GR", "en-US", "el"], "accept_language": "el-GR,el;q=0.9,en-US;q=0.8"}
    ]
    FRANCE = [
        {"locale": "fr-FR", "languages": ["fr-FR", "fr"], "accept_language": "fr-FR,fr;q=0.9"},
        {"locale": "fr-FR", "languages": ["fr-FR", "en-US", "fr"], "accept_language": "fr-FR,fr;q=0.9,en-US;q=0.8"}
    ]
    ITALY = [
        {"locale": "it-IT", "languages": ["it-IT", "it"], "accept_language": "it-IT,it;q=0.9"},
        {"locale": "it-IT", "languages": ["it-IT", "en-US", "it"], "accept_language": "it-IT,it;q=0.9,en-US;q=0.8"}
    ]
    BULGARIA = [
        {"locale": "bg-BG", "languages": ["bg-BG", "bg"], "accept_language": "bg-BG,bg;q=0.9"},
        {"locale": "bg-BG", "languages": ["bg-BG", "bg", "en-US"], "accept_language": "bg-BG,bg;q=0.9,en-US;q=0.8"},
        {"locale": "bg-BG", "languages": ["bg-BG", "bg", "en-GB"], "accept_language": "bg-BG,bg;q=0.9,en-GB;q=0.8"}
    ]
    NETHERLANDS = [
        {"locale": "nl-NL", "languages": ["nl-NL", "nl"], "accept_language": "nl-NL,nl;q=0.9"},
        {"locale": "nl-NL", "languages": ["nl-NL", "nl", "en-US"], "accept_language": "nl-NL,nl;q=0.9,en-US;q=0.8"},
        {"locale": "nl-NL", "languages": ["nl-NL", "nl", "en-GB"], "accept_language": "nl-NL,nl;q=0.9,en-GB;q=0.8"}
    ]
    SWEDEN = [
        {"locale": "sv-SE", "languages": ["sv-SE", "sv"], "accept_language": "sv-SE,sv;q=0.9"},
        {"locale": "sv-SE", "languages": ["sv-SE", "sv", "en-US"], "accept_language": "sv-SE,sv;q=0.9,en-US;q=0.8"},
        {"locale": "sv-SE", "languages": ["sv-SE", "sv", "en-GB"], "accept_language": "sv-SE,sv;q=0.9,en-GB;q=0.8"}
    ]
    ROMANIA = [
        {"locale": "ro-RO", "languages": ["ro-RO", "ro"], "accept_language": "ro-RO,ro;q=0.9"},
        {"locale": "ro-RO", "languages": ["ro-RO", "ro", "en-US"], "accept_language": "ro-RO,ro;q=0.9,en-US;q=0.8"},
        {"locale": "ro-RO", "languages": ["ro-RO", "ro", "en-GB"], "accept_language": "ro-RO,ro;q=0.9,en-GB;q=0.8"}
    ]
    CZECH = [
        {"locale": "cs-CZ", "languages": ["cs-CZ", "cs"], "accept_language": "cs-CZ,cs;q=0.9"},
        {"locale": "cs-CZ", "languages": ["cs-CZ", "cs", "en-US"], "accept_language": "cs-CZ,cs;q=0.9,en-US;q=0.8"},
        {"locale": "cs-CZ", "languages": ["cs-CZ", "cs", "en-GB"], "accept_language": "cs-CZ,cs;q=0.9,en-GB;q=0.8"}
    ]
    HUNGARY = [
        {"locale": "hu-HU", "languages": ["hu-HU", "hu"], "accept_language": "hu-HU,hu;q=0.9"},
        {"locale": "hu-HU", "languages": ["hu-HU", "hu", "en-US"], "accept_language": "hu-HU,hu;q=0.9,en-US;q=0.8"},
        {"locale": "hu-HU", "languages": ["hu-HU", "hu", "en-GB"], "accept_language": "hu-HU,hu;q=0.9,en-GB;q=0.8"},
    ]
    FINLAND = [
        {"locale": "fi-FI", "languages": ["fi-FI", "fi"], "accept_language": "fi-FI,fi;q=0.9"},
        {"locale": "fi-FI", "languages": ["fi-FI", "fi", "en-US"], "accept_language": "fi-FI,fi;q=0.9,en-US;q=0.8"},
        {"locale": "fi-FI", "languages": ["fi-FI", "fi", "en-GB"], "accept_language": "fi-FI,fi;q=0.9,en-GB;q=0.8"}
    ]







class CountryFonts(Enum):
    GERMANY = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    POLAND = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    FRANCE = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    ITALY = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    SPAIN = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    GREECE = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT",
        "Palatino Linotype", "Lucida Sans Unicode", "Constantia", "Corbel"
    ]
    NETHERLANDS = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    BULGARIA = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Segoe UI", "Tahoma", "Times New Roman", "Verdana",
        "Noto Sans", "Roboto", "PT Sans", "PT Serif", "Arial Unicode MS",
        "Lucida Sans Unicode", "Open Sans"
    ]
    SWEDEN = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    ROMANIA = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Palatino Linotype", "Lucida Sans Unicode", "Segoe UI",
        "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Roboto",
        "Noto Sans", "Franklin Gothic Medium", "Gill Sans MT"
    ]
    CZECH = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Helvetica", "Impact", "Lucida Sans Unicode", "Palatino Linotype",
        "Segoe UI", "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Arial CE", "Times New Roman CE", "Courier New CE",  
        "Microsoft Sans Serif", "Book Antiqua", "Century Gothic",
        "Franklin Gothic Medium", "Gill Sans MT", "Lucida Console",
        "Segoe UI Symbol", "Segoe UI Emoji",
        "Roboto", "Noto Sans", "Calibri Light", "Leelawadee UI", "Ebrima",
        "Corbel", "Constantia", "Cascadia Mono", "Meiryo UI", "Yu Gothic UI",
        "DejaVu Sans", "DejaVu Serif", "Open Sans", "PT Sans", "Tahoma CE",
        "Verdana CE", "Segoe Print", "Comic Sans MS"
    ]
    HUNGARY = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Helvetica", "Impact", "Lucida Sans Unicode", "Palatino Linotype",
        "Segoe UI", "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Arial CE", "Times New Roman CE", "Courier New CE", "Tahoma CE",
        "Verdana CE", "Microsoft Sans Serif", "Book Antiqua", "Century Gothic",
        "Franklin Gothic Medium", "Gill Sans MT", "Lucida Console",
        "Segoe UI Symbol", "Segoe UI Emoji", "Leelawadee UI", "Ebrima",
        "Corbel", "Constantia", "Cascadia Mono", "Calibri Light",
        "Roboto", "Noto Sans", "Open Sans", "PT Sans", "DejaVu Sans", "DejaVu Serif",
        "Comic Sans MS", "Segoe Print", "Segoe Script", "Arial Unicode MS"
    ]
    FINLAND = [
        "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
        "Georgia", "Helvetica", "Impact", "Lucida Sans Unicode", "Palatino Linotype",
        "Segoe UI", "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
        "Roboto", "Noto Sans", "Segoe UI Emoji", "Corbel", "Constantia",
        "Ebrima", "Leelawadee UI", "Malgun Gothic", "Yu Gothic UI", "Meiryo UI",
        "Comic Sans MS", "Book Antiqua", "Century Gothic", "Franklin Gothic Medium",
        "Gill Sans MT", "Calibri Light", "Nirmala UI", "Segoe Print", "Segoe Script"
    ]




    




