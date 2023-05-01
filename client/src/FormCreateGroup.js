import React, {useState} from "react";
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'



function FormCreateGroup() {



    return (
        <Form className='addForm' onSubmit={handleSubmit}>
            <div>
                <Form.Control onChange={handleGroupName} type='text' name='title' placeholder='Title'/>
            </div>
            <Button className='add-button' type='submit'>Create A Group</Button>
            <Button className='add-button' onClick={handleHideForm}>Close Form</Button>
        </Form>
    )
}

export default FormCreateGroup;
