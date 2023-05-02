import React, {useState, useHistory} from "react"
import { useFormik } from 'formik'
import * as yup from 'yup'
import Form from 'react-bootstrap'


function PageLogin({updateUser}) {
    const [ signUp, setSignUp ] = useState(false)
    const history = useHistory()

    const handleClick = () => setSignUp((signUp) => !signUp)






    const formSchema = yup.object().shape({
        username: yup.string().required('Please enter a username'),
        email: yup.string().email(),
        password: yup.string()
    })

    const formik = useFormik({
        initialValues:{
            name:'',
            email:'',
            password:''
        },
        validationSchema:formSchema,
        onSubmit:(values) => {
            fetch(signUp?'/users':'/login',{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(r => r.json())
            .then(user => {
                updateUser(user)
                history.push('/')
            })

        }
    })

        return (
            <>
            {Object.values(formik.errors).map(error => <h2 style={{color:'red'}}>{error}</h2>)}
            <h2>Please Log in or Sign up!</h2>
            <h2>{signUp?'Already a member?':'Not a member?'}</h2>
            <button onClick={handleClick}>{signUp?'Log in!':'Register now!'}</button>
            
            <Form className='login-create' onSubmit={formik.handleSubmit}>
                <div>
                    {signUp?(
                        <>
                        <input onChange={formik.handleChange} type='text' value={formik.values.username} name='Username' placeholder='Username'/>
                        <input onChange={formik.handleChange} type='text' value={formik.values.email} name='Email' placeholder='Email'/>
                        <input onChange={formik.handleChange} type='text' value={formik.values.password} name='title' placeholder='Password'/>
                        </>
                    ):
                        <>
                        <input onChange={formik.handleChange} type='text' value={formik.values.email} name='Email' placeholder='Email'/>
                        <input onChange={formik.handleChange} type='text' value={formik.values.password} name='title' placeholder='Password'/>
                        </>
                    }
                </div>
            </Form>
            </>
        )
}

export default PageLogin;
