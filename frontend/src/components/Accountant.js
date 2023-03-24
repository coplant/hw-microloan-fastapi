import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {accountant, logout, pay} from '../APIs';

function Accountant() {
    const navigate = useNavigate();
    const [users, setUsers] = useState([]);

    useEffect(() => {
        accountant()
            .then((response) => response.json())
            .then((result) => {
                setUsers(result.data);
            });
    }, [users]);

    const handleLogout = async () => {
        const response = await logout();
        const res = await response.json();
        if (response.ok == true) {
            navigate('/login');
        } else {
            alert(res.detail);
        }
    };
    const handleSubmit = async (id) => {
        const response = await pay(id);
        const res = await response.json();
        alert(res.detail);
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
                <h2 className='text-2xl font-bold text-center text-white pt-10 mb-5'>
                    Accountant menu
                </h2>
                {users.length == 0 ? null : (
                    <div className='overflow-x-auto  sm:rounded-lg mx-5 mb-10'>
                        <table className='w-full text-sm text-left text-white '>
                            <thead className='text-xs text-white uppercase bg-orange-500'>
                            <tr>
                                <th className='px-6 py-3'>Creation Date</th>
                                <th className='px-6 py-3'>End Date</th>
                                <th className='px-6 py-3'>Amount</th>
                                <th className='px-6 py-3'>Period</th>
                                <th className='px-6 py-3'>Status</th>
                                <th className='px-6 py-3'>First Name</th>
                                <th className='px-6 py-3'>Last Name</th>
                                <th className='px-6 py-3'>Middle Name</th>
                                <th className='px-6 py-3'>Passport</th>
                                <th className='px-6 py-3'>Pay</th>
                            </tr>
                            </thead>
                            <tbody>
                            {users.map((user) => (
                                <tr key={user.id} className='bg-orange-300'>
                                    <td className='px-6 py-4'>{user.creation_date}</td>
                                    <td className='px-6 py-4'>{user.end_date}</td>
                                    <td className='px-6 py-4'>{user.amount}</td>
                                    <td className='px-6 py-4'>{user.period}</td>
                                    <td className='px-6 py-4'>{user.status}</td>
                                    <td className='px-6 py-4'>{user.user.first_name}</td>
                                    <td className='px-6 py-4'>{user.user.last_name}</td>
                                    <td className='px-6 py-4'>{user.user.middle_name}</td>
                                    <td className='px-6 py-4'>{user.user.passport.number}</td>
                                    <td className='cursor-pointer bg-green-500  ml-2 hover:bg-green-700'>
                                        <button
                                            className='w-full h-12'
                                            onClick={() => {
                                                handleSubmit(user.user.id);
                                            }}
                                        >
                                            Confirm
                                        </button>
                                    </td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </>
    );
}

export default Accountant;
