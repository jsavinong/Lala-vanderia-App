from flet import *
from utils.extras import *

class SignupPage(Container):
  def __init__(self,):
    super().__init__()
    #self.email = email
    #self.dp_url = dp
    self.offset = transform.Offset(0,0,)
    self.expand = True

    self.pwd_input =  Container(
            height=altura_btn,
            bgcolor="white",
            border_radius=10,
            content=TextField(
                hint_text="Contraseña",
                hint_style=TextStyle(
                    size=16,
                    color=input_hint_color
                ),
                text_style=TextStyle(
                    size=16,
                    color=input_hint_color
                ),
                border=InputBorder.NONE,
                content_padding=content_padding

            )
        )

    self.signup_box = Column(
        controls=[
            Column(
                spacing=0,
                controls=[
                Text(
                    value=f'Al parecer no tienes una cuenta con nosotros.\nAsí que vamos a crear una para',
                    size=14,
                    
                    color='#ccffffff'
                ),
                Text(
                    value="test@gmail.com",
                    size=14,
                    
                    color='#ccffffff'
                ),
                ]
            ),
            self.pwd_input,
            Container(
                height=altura_btn,
                width=anchura_btn,
                bgcolor=blue_base,
                border_radius=10,
                alignment=alignment.center,
                content=Text(
                    value='Continuar',
                    size=18, 
                )
            ),

                Container(height=20),

                Text(
                value="Olvidaste tu contraseña?",
                color=gray_base,
                size=16,
                
                ),

        ]
            )
    self.content = Container(
        height=altura_base,
        width=anchura_base,
        bgcolor="color_base",
        border_radius=radio_borde,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        content=Stack(
            controls=[
                Container(
                    height=altura_base,
                    width=anchura_base,
                    bgcolor=colors.BLACK,
                    content=Image(
                        src="assets\images\gianluca-d-intino-vl4QuDMyeyY-unsplash (1).jpg",
                        #bgcolor="#cc2d2b2c",
                        #scale=1.5,
                        fit=ImageFit.COVER,
                        opacity=0.5                       
                        
                    )
                ),
                Container(
                    height=altura_base,
                    width=anchura_base,
                    padding=padding.only(top=30, left=10,right=10),
                    content=Column(
                        controls=[
                            Container(
                              data="main_page",
                              content=Icon(
                                icons.ARROW_BACK_IOS_OUTLINED,
                                size=28
                              )
                            ),
                            Container(height=160),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value="Sign Up", 
                                    weight=FontWeight.BOLD,
                                    size=30,
                                    
                                )
                            ),
                            Container(height=2),
                            Container(
                                padding=20,
                                bgcolor="#cc2d2b2c",
                                border_radius=10,
                                content=self.signup_box
                            )
                        ]
                    )
                )
            ]
        )
    )