using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class menu : MonoBehaviour
{
    public GameObject menu_inicial;
    public GameObject login;
    public GameObject register;

    public GameObject loggedin_menu;
    public GameObject menu_canje;
    public GameObject murio;

    public GameObject juego;
    private GameObject current;
    public register registrar;
    // Start is called before the first frame update
    void Start()
    {
        poner_todo_en_falso();
        menu_inicial.gameObject.SetActive(true);
        Time.timeScale = 1;
    }
    public void btn_login()
    {
        poner_todo_en_falso();
        Debug.Log("se pulso el boton de login");
        login.gameObject.SetActive(true);
    }
    public void btn_register()
    {
        poner_todo_en_falso();
        Debug.Log("se pulso_register");
        register.gameObject.SetActive(true);


    }
    public void btn_menuinicial()
    {
        poner_todo_en_falso();
        Debug.Log("se pulso_register");
        menu_inicial.gameObject.SetActive(true);
    }
    public void btn_try_log()
    {
        Debug.Log("intentar login");
        //log in bien hecho 
        poner_todo_en_falso();
        loggedin_menu.gameObject.SetActive(true);
    }
    public void btn_canje()
    {
        
        Debug.Log("se pulso_canje");
        //el request para canje 


    }
    public void btn_playgame()
    {
        Debug.Log("play game");
        poner_todo_en_falso();

        current = Instantiate(juego);
        current.transform.position = transform.position;



    }
    
    private void poner_todo_en_falso()
    {
        login.gameObject.SetActive(false);
        register.gameObject.SetActive(false);
        menu_inicial.gameObject.SetActive(false);
        loggedin_menu.gameObject.SetActive(false);
        menu_canje.gameObject.SetActive(false);
        murio.gameObject.SetActive(false);
        
    }


    public void GameOver()
    {
        poner_todo_en_falso();
        murio.SetActive(true);
      
        Destroy(current);

    }

}
