import React, {useState} from 'react';
import {Link, useNavigate} from 'react-router-dom';
import {register} from '../APIs';

function Reg() {
    const navigate = useNavigate();
    const [user, setUser] = useState({
        email: '',
        password: '',
        first_name: '',
        middle_name: '',
        last_name: '',
        number: '',
    });

    const handleSubmit = async (user) => {
        const response = await register(user);
        const res = await response.json();
        if (response.ok == true) {
            navigate('/login');
        } else {
            alert(res.detail);
        }
    };

    const handleChange = (e) => {
        const {
            target: {value},
        } = e;
        const {
            target: {id},
        } = e;
        const copy = {...user};
        if (id == 'email') {
            copy.email = value;
            setUser(copy);
        }
        if (id == 'password') {
            copy.password = value;
            setUser(copy);
        }
        if (id == 'firstName') {
            if (/^[A-ZА-ЯЁ]+$/i.test(value) || value.length == 0) {
                copy.first_name = value;
                setUser(copy);
            }
        }
        if (id == 'middleName') {
            if (/^[A-ZА-ЯЁ]+$/i.test(value) || value.length == 0) {
                copy.middle_name = value;
                setUser(copy);
            }
        }
        if (id == 'lastName') {
            if (/^[A-ZА-ЯЁ]+$/i.test(value) || value.length == 0) {
                copy.last_name = value;
                setUser(copy);
            }
        }
        if (id == 'passport') {
            if (/^[0-9]+$/i.test(value) && value.length <= 10) {
                const copy = {...user};
                copy.number = value;
                setUser(copy);
            }
        }
    };

    return (
        <>
            <div className='max-w-xs mx-auto'>
                <div className='text-2xl font-bold text-center text-gray-800'>
                    Registration
                </div>
                <form
                    className='bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4'
                    onSubmit={(e) => {
                        e.preventDefault();
                        handleSubmit(user);
                    }}
                >
                    <div className='mb-4'>
                        <label
                            className='block text-gray-700 text-sm font-bold mb-2'
                            htmlFor='email'
                        >
                            Email
                        </label>
                        <input
                            className='shadow appearance-none border rounded py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline w-full'
                            id='email'
                            value={user.email}
                            placeholder='Enter email'
                            type='email'
                            onChange={handleChange}
                        />
                    </div>
                    <div className='mb-4'>
                        <label
                            className='block text-gray-700 text-sm font-bold mb-2'
                            htmlFor='password'
                        >
                            Password
                        </label>
                        <input
                            className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                            id='password'
                            value={user.password}
                            placeholder='Enter password'
                            type='password'
                            onChange={handleChange}
                        />
                    </div>
                    <div className='mb-4'>
                        <label
                            className='block text-gray-700 text-sm font-bold mb-2'
                            htmlFor='firstName'
                        >
                            First Name
                        </label>
                        <input
                            className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                            id='firstName'
                            value={user.first_name}
                            placeholder='Enter First Name'
                            onChange={handleChange}
                        />
                    </div>
                    <div className='mb-4'>
                        <label
                            className='block text-gray-700 text-sm font-bold mb-2'
                            htmlFor='middleName'
                        >
                            Middle Name
                        </label>
                        <input
                            className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                            id='middleName'
                            value={user.middle_name}
                            placeholder='Enter Middle Name'
                            onChange={handleChange}
                        />
                    </div>
                    <div className='mb-4'>
                        <label
                            className='block text-gray-700 text-sm font-bold mb-2'
                            htmlFor='lastName'
                        >
                            Last Name
                        </label>
                        <input
                            className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                            id='lastName'
                            value={user.last_name}
                            placeholder='Enter Last Name'
                            onChange={handleChange}
                        />
                    </div>
                    <div className='mb-6'>
                        <label
                            className='block text-gray-700 text-sm font-bold mb-2'
                            htmlFor='passport'
                        >
                            Passport
                        </label>
                        <input
                            className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                            id='passport'
                            value={user.number}
                            placeholder='Enter passport'
                            type='text'
                            onChange={handleChange}
                        />
                    </div>
                    <button
                        className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 mb-4 border-b-4 border-orange-700 hover:border-orange-500 rounded mr-2 text-center w-full'>
                        Register
                    </button>
                    <div className='flex flex-col'>
                        <Link className='font-bold hover:text-orange-500' to='/login'>
                            Already have account?
                        </Link>
                        <Link
                            className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 border-b-4 border-orange-700 hover:border-orange-500 rounded mr-2 text-center w-full mt-5'
                            to='/'
                        >
                            Back to home
                        </Link>
                    </div>
                </form>
            </div>
        </>
    );
}

export default Reg;
