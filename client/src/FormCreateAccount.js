import React, {useState} from "react"
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'



function FormCreateAccount() {



    return (
        <Form className='addForm' onSubmit={handleSubmit}>
        <div>
            <Form.Control onChange={handleUsername} type='text' name='Username' placeholder='Username'/>
            <Form.Control onChange={handleEmail} type='text' name='Email' placeholder='Email'/>
            <Form.Control onChange={handlePassword} type='text' name='title' placeholder='Password'/>
            <Form.Control onChange={handlePasswordConfirmation} type='text' name='title' placeholder='Password Confirmation'/>
        </div>
        <Button className='add-button' type='submit'>Add A Character</Button>
        <Button className='add-button' onClick={handleHideForm}>Close Form</Button>
    </Form>
    )
}

export default FormCreateAccount;
