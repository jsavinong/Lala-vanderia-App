import threading
from flet import *
import httpx
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to, go_back
from translations import load_translations, gettext as _


def planes_page_view(page: Page, params: Params=None, basket: Basket=None):
    
    selected_index = get_state("selected_nav_index", default=0)
    
    

    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    
    def handle_subscription(page: Page, plan_name: str):
    #  Lógica para realizar la llamada a la API
        print(f"Suscribiendo al plan {plan_name}")
        subscribe_user(page, plan_id, on_subscription_result)


    def subscribe_user(page: Page, plan_id: int, callback):
        def do_subscribe():
            url = f"http://127.0.0.1:8000/subscribe/{plan_id}"
            # Asumiendo que tienes algún método para obtener el token de acceso
            headers = {"Authorization": f"Bearer {get_state('access_token')}"}
            try:
                with httpx.Client() as client:
                    response = client.post(url, headers=headers)
                    if response.status_code == 200:
                        callback(True, "Suscripción exitosa")
                    else:
                        callback(False, "Error en la suscripción")
            except Exception as e:
                callback(False, str(e))
        threading.Thread(target=do_subscribe).start()

    def on_subscription_result(success, message):
        if success:
            page.snack_bar(SnackBar(content=Text(message)))
        else:
            page.snack_bar(SnackBar(content=Text(f"Error: {message}")))

    
    container_go_back = Container(
        on_click = lambda e: go_back(page),
        content=Icon(
            icons.ARROW_BACK_IOS_OUTLINED, size=28, color="#f0fdfa"
        ),
        width=30, 
        alignment=alignment.center_left
    )
    
    container_name = Container(
        content=Row(
            controls=[
                container_go_back,
                Text(
                    value=_("plans"), 
                    weight=FontWeight.BOLD, 
                    size=24,color="#f0fdfa"),
                
            ]
        ),
        padding=Padding(15,20,5,15),
        bgcolor="#042f2e",
        width=anchura_base,
        height=80
    )


    planes_text_title = Text(
        value=_("pick_plan"), style=TextStyle(size=24, weight=FontWeight.BOLD, color="f0fdfa")
    )

    plan_small__text_name = Text(value=_("plan_small"),weight=FontWeight.W_500, 
        size=24,color="#042f2e") 
    
    plan_small_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=200,
        height=altura_btn,  
        on_click=lambda e: handle_subscription(page, "Plan Pequeño"),
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor= "#0f766e",color="#f0fdfa")

)
    plan_small_container = Container(
        content=Column(
            controls=[
            
                plan_small__text_name,
                plan_small_btn
            ],horizontal_alignment=CrossAxisAlignment.CENTER, 
            alignment=MainAxisAlignment.CENTER
        ),
        
        image_src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/Plan Small.jpg",
        image_fit=ImageFit.COVER,
        height=400,
        width= 250,
        border_radius=50,
        bgcolor=colors.WHITE60
        
        
    )

    plan_medium__text_name = Text(value=_("plan_medium"),weight=FontWeight.W_500, 
        size=24,color="#042f2e") 
    
    plan_medium_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=200,
        height=altura_btn,  
        on_click=lambda e: handle_subscription(page, "Plan Medio"),
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor= "#0f766e",color="#f0fdfa")
                
)
    plan_medium_container = Container(
        content=Column(
            controls=[
            
                plan_medium__text_name,
                plan_medium_btn
            ],horizontal_alignment=CrossAxisAlignment.CENTER, 
            alignment=MainAxisAlignment.CENTER
        ),
        
        image_src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/Plan Medium.jpg",
        image_fit=ImageFit.COVER,
        height=400,
        width= 250,
        border_radius=50,
        bgcolor=colors.WHITE60
        
        
    )

    plan_large__text_name = Text(value=_("plan_large"),weight=FontWeight.W_500, 
        size=24,color="#042f2e") 
    
    plan_large_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=200,
        height=altura_btn,  
        on_click=lambda e: handle_subscription(page, "Plan Grande"),
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor= "#0f766e",color="#f0fdfa")
                
)
    plan_large_container = Container(
        content=Column(
            controls=[
            
                plan_large__text_name,
                plan_large_btn
            ],horizontal_alignment=CrossAxisAlignment.CENTER, 
            alignment=MainAxisAlignment.CENTER
        ),
        
        image_src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/Plan Large.jpg",
        image_fit=ImageFit.COVER,
        height=400,
        width= 250,
        border_radius=50,
        bgcolor=colors.WHITE60
        
        
    )

    planes_row = Row(
        controls=[
                Container(width=10),
                plan_small_container,
                Container(width=10),
                plan_medium_container,
                Container(width=10),
                plan_large_container,
                Container(width=10),

        ],scroll="auto",
        vertical_alignment=CrossAxisAlignment.CENTER,
        alignment=MainAxisAlignment.SPACE_EVENLY,
        spacing=50,
        )


    
    content = Container(
    
        #height=altura_base,
        width=anchura_base,
        bgcolor="#3309252a",
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        
        content=Column(
            controls=[
                Container(height=10),
                planes_text_title,
                Container(height=10),
                planes_row,
                Container(height=10),
                # faq_textbtn,
                # terminos_de_uso_textbtn,
                

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
            ),
        
        
    )

    main_container = Container(
        expand=True,
        content=Stack(
            [
                Container(
                    gradient=LinearGradient(
                        rotation=30,
                        begin=alignment.center_left,
                        end=alignment.bottom_right,
                        colors=["#CC09252a", "#CCd2f5f4"],
                    ),
                ),
                Container(
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Container(
                                width=anchura_base,
                                height=700,
                                content=Column(
                                    controls=[
                                        container_name,
                                        content,
                                        
                                        #dashboard_content,
                                    ]
                                ),
                            )
                        ]
                    ),
                ),
  
            ],
        ),
    )
    
    return View("/planes", controls=[main_container ])
