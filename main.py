import flet as ft

import diccionario
import silabeador
import entonacion

D = diccionario.leerDiccionario()

def main(page: ft.Page):
    page.title = "Proyecto ALF"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    def salir(e):
        diccionario.escribirDiccionario(D)
        page.window_destroy()
        exit(0)


    def desarrollo(e):
        page.clean()
        ponerOpciones()
        page.add(
            ft.Row(
                [
                    ft.Text("En desarrollo...", color="pink")
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Text("")
                ]
            )
        )


    def ponerBotonPalabraSilabar(e):
        def silabear(e):
            if not pal.value:
                pal.error_text = "Introduce una palabra"
                page.update()
            else:
                palabra = str(pal.value)
                res = diccionario.comprobar(palabra, D)
                if res == []:
                    silabas = silabeador.silabear(palabra)
                    diccionario.insertarSilabas(palabra, silabas, D)
                else:
                    if res[0] != []:
                        silabas = res[0]
                    else:
                        silabas = silabeador.silabear(palabra)
                        diccionario.insertarSilabas(palabra, silabas, D)
                page.add(
                    ft.Row(
                        [
                            ft.Text(str(palabra) + " -> " + str(silabas), color="orange")
                        ], alignment=ft.MainAxisAlignment.CENTER
                    )
                )

        pal = ft.TextField(label="Introduce una palabra para silabear")
        page.clean()
        ponerOpciones()
        page.add(
            ft.Row(
                [
                    pal,
                    ft.ElevatedButton("Enviar", on_click=silabear)
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        )


    def ponerBotonPalabraEntonar(e):
        def entonar(e):
            if not pal.value:
                pal.error_text = "Introduce una palabra"
                page.update()
            else:
                palabra = str(pal.value)
                res = diccionario.comprobar(palabra, D)
                if res == []:
                    ent = entonacion.entonacion(palabra)
                    diccionario.insertarEntonacion(palabra, ent, D)
                else:
                    if res[1] != '':
                        ent = res[1]
                    else:
                        ent = entonacion.entonacion(palabra)
                        diccionario.insertarEntonacion(palabra, ent, D)
                page.add(
                    ft.Row(
                        [
                            ft.Text(str(palabra) + " es " + ent + ".", color="orange")
                        ], alignment=ft.MainAxisAlignment.CENTER
                    )
                )

        pal = ft.TextField(label="Introduce una palabra para entonar")
        page.clean()
        ponerOpciones()
        page.add(
            ft.Row(
                [
                    pal,
                    ft.ElevatedButton("Enviar", on_click=entonar)
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        )


    def ponerOpciones():
        page.add(
            ft.Row(
                [ft.Text("OPCIONES:", color="orange", size=20, weight=ft.FontWeight.BOLD)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ft.TextButton("1. Silabear una palabra.", on_click=ponerBotonPalabraSilabar)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ft.TextButton("2. Clasificar una palabra según su entonación.", on_click=ponerBotonPalabraEntonar)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ft.TextButton("3. Obtener palabras que rimen con una dada.", on_click=desarrollo)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ft.TextButton("4. Justificar un texto.", on_click=desarrollo)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ft.TextButton("5. Salir.", on_click=salir)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
    page.add(
        ft.Row(
            [ft.Text("PROYECTO FINAL PRÁCTICAS - AUTÓMATAS Y LENGUAJES FORMALES", color="orange", size=20, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.Text("")],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    ponerOpciones()


ft.app(target=main)