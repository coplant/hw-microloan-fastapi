import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {
  logout,
  userChangeAdmin,
  userDeleteAdmin,
  userInfo,
  userInfoAdmin,
} from '../APIs';

function Admin() {
  const navigate = useNavigate();
  const [user, setUser] = useState({
    id: null,
    email: '',
    password: '',
    firstName: '',
    middleName: '',
    lastName: '',
  });

  useEffect(() => {
    userInfo()
        .then((response) => response.json())
        .then(async (res) => {
          if (res.role_id != 100) {
            navigate('/');
          }
        });
  }, []);

  const handleSubmit = async () => {
    const userID = document.querySelector('#userId');
    const response = await userInfoAdmin(userID.value);
    const res = await response.json();
    setUser({
      id: res.id,
      email: res.email,
      firstName: res.first_name,
      middleName: res.middle_name,
      lastName: res.last_name,
    });
    if (response.ok == false) {
      alert(res.detail);
    }
  };

  const handleChange = async () => {
    const inputs = document.querySelectorAll('input');
    if (
        inputs[1].value.length != 0 ||
        inputs[2].value.length != 0 ||
        inputs[3].value.length != 0 ||
        inputs[4].value.length != 0 ||
        inputs[5].value.length != 0
    ) {
      if (
          /^[A-ZА-ЯЁ]+$/i.test(inputs[3].value) &&
          /^[A-ZА-ЯЁ]+$/i.test(inputs[4].value) &&
          /^[A-ZА-ЯЁ]+$/i.test(inputs[5].value)
      ) {
        const response = await userChangeAdmin(user, inputs);
        const res = await response.json();
        setUser({
          id: res.id,
          email: res.email,
          firstName: res.first_name,
          middleName: res.middle_name,
          lastName: res.last_name,
        });
      } else if (
          inputs[3].value.length != 0 ||
          inputs[4].value.length != 0 ||
          inputs[5].value.length != 0
      ) {
        alert('Некорректные данные ФИО');
      }
    } else {
      alert('Вы ничего не ввели!');
    }
  };

  const handleDelete = async () => {
    const response = await userDeleteAdmin(user.id);
    console.log(response);
    setUser({
      id: null,
      email: '',
      password: '',
      firstName: '',
      middleName: '',
      lastName: '',
    });
  };

  const handleLogout = async () => {
    let response = await logout();
    let res = await response.json();
    if (response.ok == true) {
      navigate('/login');
    } else {
      alert(res.detail);
      alert();
    }
  };

  return (
      <>
        <nav className='bg-orange-300 border-gray-200 px-4 lg:px-6 py-2.5'>
          <div className='flex flex-wrap justify-end items-center mx-auto max-w-screen-xl'>
            <button
                onClick={handleLogout}
                className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 border-b-4 border-orange-700 hover:border-orange-500 rounded mr-2 w-1/6 text-center'
            >
              Log Out
            </button>
          </div>
        </nav>
        <div className='bg-orange-200 min-h-screen'>
          <h2 className='text-2xl font-bold text-center text-white pt-10'>
            Administrator menu
          </h2>
          <section className='container mx-auto p-5 w-1/2'>
            <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleSubmit();
                }}
                className='mx-20 text-white gap-10 mt-10'
            >
              <div className='mb-6'>
                <label
                    className='block text-white text-sm font-bold mb-2'
                    htmlFor='userId'
                >
                  Select User
                </label>
                <input
                    className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                    id='userId'
                    placeholder='Enter user ID'
                    type='text'
                />
                <button
                    className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 mb-4 border-b-4 border-orange-700 hover:border-orange-500 mt-2 rounded mr-2 text-center w-full'>
                  Confirm
                </button>
              </div>
            </form>
            <div className='flex flex-col text-white text-2xl'>
              <span>ID: {user.id}</span>
              <span>Email: {user.email}</span>
              <span>First Name: {user.firstName}</span>
              <span>Middle Name: {user.middleName}</span>
              <span>Last Name: {user.lastName}</span>
            </div>
            <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleChange(user.id);
                }}
                className='grid grid-cols-2 text-white gap-10 mt-10'
            >
              <div className='mb-6'>
                <label
                    className='block text-white text-sm font-bold mb-2'
                    htmlFor='email'
                >
                  Email
                </label>
                <input
                    className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                    id='email'
                    placeholder='Enter email'
                    type='text'
                />
              </div>
              <div className='mb-6'>
                <label
                    className='block text-white text-sm font-bold mb-2'
                    htmlFor='password'
                >
                  Password
                </label>
                <input
                    className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                    id='password'
                    placeholder='Enter password'
                    type='text'
                />
              </div>
              <div className='mb-6'>
                <label
                    className='block text-white text-sm font-bold mb-2'
                    htmlFor='passport'
                >
                  First Name
                </label>
                <input
                    className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                    id='firstName'
                    placeholder='Enter First Name'
                    type='text'
                />
              </div>
              <div className='mb-6'>
                <label
                    className='block text-white text-sm font-bold mb-2'
                    htmlFor='passport'
                >
                  Middle Name
                </label>
                <input
                    className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                    id='middleName'
                    placeholder='Enter Middle Name'
                    type='text'
                />
              </div>
              <div className='mb-6'>
                <label
                    className='block text-white text-sm font-bold mb-2'
                    htmlFor='lastName'
                >
                  Last Name
                </label>
                <input
                    className='shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full'
                    id='lastName'
                    placeholder='Enter Last Name'
                    type='text'
                />
              </div>
              <button
                  className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 mb-4 border-b-4 border-orange-700 hover:border-orange-500 mt-2 rounded mr-2 text-center w-full'>
                Change User Data
              </button>
            </form>
            <button
                onClick={handleDelete}
                className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 mb-4 border-b-4 border-orange-700 hover:border-orange-500 mt-2 rounded mr-2 text-center w-full'
            >
              Delete User
            </button>
          </section>
        </div>
      </>
  );
}
export default Admin;