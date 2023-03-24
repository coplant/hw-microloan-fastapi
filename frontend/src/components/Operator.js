import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {loadPassport, logout, operation, verify} from '../APIs';

const baseImage = 'https://klike.net/uploads/posts/2022-06/1654842544_1.jpg';

function Operator() {
    const navigate = useNavigate();
    const [image, setImage] = useState(baseImage);

    const [unverifs, setUnverifs] = useState([]);
    useEffect(() => {
        operation()
            .then((response) => response.json())
            .then((res) => {
                setUnverifs(res.data);
            });
    }, [unverifs]);

    const handleLogout = async () => {
        const response = await logout();
        const res = await response.json();
        if (response.ok == true) {
            navigate('/login');
        } else {
            alert(res.detail);
            alert();
        }
    };

    const handleImage = async (src) => {
        const response = await loadPassport(src);
        const res = await response.blob();
        setImage(URL.createObjectURL(res));
        if (response.ok == false) {
            alert(res.detail);
        }
    };

    const handleVerify = async (src) => {
        const response = await verify(src);
        setImage(baseImage);
        const res = await response.json();
        if (response.ok == false) {
            alert(res.detail);
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
                <h2 className='text-2xl font-bold text-center text-white pt-10 mb-5'>
                    Operator menu
                </h2>
                {unverifs.length == 0 ? null : (
                    <div className='overflow-x-auto  sm:rounded-lg mx-5'>
                        <table className='w-full text-sm text-left text-white '>
                            <thead className='text-xs text-white uppercase bg-orange-500'>
                            <tr>
                                <th className='px-6 py-3'>Name</th>
                                <th className='px-6 py-3'>Middle Name</th>
                                <th className='px-6 py-3'>Last Name</th>
                                <th className='px-6 py-3'>Email</th>
                                <th className='px-6 py-3'>Registered Date</th>
                                <th className='px-6 py-3'>Passport</th>
                                <th className='px-6 py-3'>Filename</th>
                                <th className='px-6 py-3'>Verify</th>
                            </tr>
                            </thead>
                            <tbody>
                            {unverifs.map((unverif) => (
                                <tr key={unverif.passport_id} className='bg-orange-400'>
                                    <td className='px-6 py-4'>{unverif.user.first_name}</td>
                                    <td className='px-6 py-4'>{unverif.user.middle_name}</td>
                                    <td className='px-6 py-4'>{unverif.user.last_name}</td>
                                    <td className='px-6 py-4'>{unverif.user.email}</td>
                                    <td className='px-6 py-4'>{unverif.user.registered_at}</td>
                                    <td className='px-6 py-4'>{unverif.number}</td>
                                    <td>
                                        <button
                                            className='w-full h-12'
                                            onClick={() => handleImage(unverif.filename)}
                                        >
                                            Check the passport
                                        </button>
                                    </td>
                                    <td>
                                        <button
                                            className='w-full h-12'
                                            onClick={() => handleVerify(unverif.user.user_id)}
                                        >
                                            Verify
                                        </button>
                                    </td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    </div>
                )}
                <div className='mx-auto w-1/2 mt-10'>
                    <img className='w-full' src={image}></img>
                </div>
            </div>
        </>
    );
}

export default Operator;
