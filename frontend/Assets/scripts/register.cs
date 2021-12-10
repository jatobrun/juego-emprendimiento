using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.Networking;
public class register : MonoBehaviour
{
    public TMP_InputField usuario,contra,correo,cedula,numero;
    private string ocedula, onombre, oapellido, ocorreo, otelefono, ousuario, ocontraseña;
    public void try_regist()
    {
        ousuario = usuario.textComponent.text;
        ocontraseña = contra.textComponent.text;
        ocorreo = correo.textComponent.text;
        ocedula = cedula.textComponent.text;
        otelefono = numero.textComponent.text;
        onombre = "andress";
        oapellido = "castro";
        StartCoroutine(Upload());
    }

    IEnumerator Upload()
    {
       

       
        

        string str = "cedula="+ocedula+"&nombre="+onombre+"&apellido="+oapellido+"&correo="+ocorreo+"&telefono="+otelefono+"&usuario="+ousuario+"&contraseña="+ocontraseña;
        string uri = "http://api.turisteando.xyz/registro?"+str;

        UnityWebRequest uwr = UnityWebRequest.Get(uri);
        yield return uwr.SendWebRequest();

        if (uwr.isNetworkError)
        {
            Debug.Log("Error While Sending: " + uwr.error);
        }
        else
        {
            Debug.Log("Received: " + uwr.downloadHandler.text);
        }
    }
}


