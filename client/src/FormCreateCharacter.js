import React, {useState} from "react"
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'



function FormCreateCharacter() {



    return (
        <Form className='addForm' onSubmit={handleSubmit}>
        <div>
            <Form.Control onChange={handleCharacterName} type='text' name='Character-name' placeholder='Character Name'/>
            <Form.Control onChange={handleCharacterRace} type='text' name='title' placeholder='Character Race'/>
            <Form.Control onChange={handleCharacterClass} type='text' name='title' placeholder='Character Class'/>
        </div>
        <Button className='add-button' type='submit'>Add A Character</Button>
        <Button className='add-button' onClick={handleHideForm}>Close Form</Button>
    </Form>
    )
}

export default FormCreateCharacter;
