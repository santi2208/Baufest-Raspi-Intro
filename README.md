<h1>Raspi - Intro</h1>

<p>Este repositorio contiene el material necesario para realizar una charla introductoria a Raspberry Pi y la interacción básica con módulos digitales.</p>
<p>El repositorio consta de:</p>
<h1><a id="Documentacion_9"></a>Documentacion</h1>
<ul>
<li>Presentacion: Se encuentra un presentación que puede ser utilizada para guiar una primera charla introductoria.<br>
Esta presentación está casi desprovista de textos. Es un soport visual para llevar y guiar la charla.<br>
No esta pensada para ser un material de consulta</li>
<li>Diagrama de conexión: Se trata de un diagrama sencillo que muestra cómo deben estar conectados los módulos para que la lógica de cada uno de los ejemplos funcione correctamente.</li>
</ul>
<h1><a id="ControlModules_16"></a>ControlModules</h1>
<p>Esta carpeta contiene ejemplos segmentados para ejercitar interacciones con distintos módulos digitales:</p>
<ul>
<li>00_Test: Es un pequeño programa que prueba de forma simple y parametrizada que cada uno de los módulos conectados funcionen correctamente. Usualmente se suele correr antes de cada presentación para validar que ningún cable esté suelto y que todo funciona correctamente.</li>
<li>01_Led: Ejercitación orientada a realizar un primer contacto con “el seteo” del valor de un pin del gpio. Se añade además el primer contacto con el uso de PWM.</li>
<li>02_MovementDetection: Ejercitación orientada a interactuar con un sensor de movimiento PIR.</li>
<li>03_DistanceDetection: Ejercitación orientada a interactuar con un sensor de distancia por ultrasonido.</li>
<li>04_SwitchController: Ejercitación orientada a interactuar con un relay.</li>
<li>05_ServoController: Ejercitación orientada a interactuar con un servo motor y reforzar el uso de la librería de PWM.</li>
<li>06_StepperController: Ejercitación orientada a interactuar con un motor “Paso a Paso” (Stepper motor). Cuenta con una clase cuya función es la de abstraer la lógica  de manejo específico del motor paso a paso de 4 bobinas.</li>
<li>Integrador_1: Contiene la resolución para distintos cortes (distintos niveles de avance) de posible ejercitación propuesta a fin de unir en un solo contexto los distintos módulos vistos anteriormente.</li>
<li>Integrador_2: Contiene la resolución para distintos cortes (distintos niveles de avance) de posible ejercitación propuesta a fin de manejar cada uno de los módulos mediante mensajes UDP (parametrizables) que se manden desde una IP local. Se recomienda bajar alguna aplicación mobile que pueda mandar mensajes UDP a una ip:puerto.</li>
</ul>
<h1><a id="GpioWatcher_28"></a>GpioWatcher</h1>
<p>Contiene un pequeño programa que se encarga de leer periodicamente los estados de los pines que se ven involucrados en la ejercitación. Al cambiar el valor de alguno, informa este cambio a una URL parametrizable.<br>
Este programa provee de información al GpioReceiver, que se encarga de mostrarla en un pequeño y simple tablero de control.</p>
<h1><a id="GpioReceiver_32"></a>GpioReceiver</h1>
<p>Contiene un pequeño servidor en node que se encarga de recibir el estado de cada uno de los módulos intervinientes en la práctica y con esta información, utilizando web sockets y knockout.js, podemos visualizar un pequeño tablero de control con el estado en vivo de cada uno de los módulos por equipo interviniente.</p>
<h1><a id="Services_35"></a>Services</h1>
<p>Cuenta con un único servicio que se encarga de manejar la interacción con mensajes UDP.</p>
