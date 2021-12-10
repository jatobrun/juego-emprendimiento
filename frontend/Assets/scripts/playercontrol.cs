using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playercontrol : MonoBehaviour
{
    public float velocidad = 1;
    private Rigidbody2D rb;
  

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();    
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            rb.velocity = Vector3.up * velocidad;
        }
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        menu objeto2 = GameObject.Find("manager").GetComponent<menu>();
        objeto2.GameOver();
    }
}
