from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='zachary',
    author_email='zlj19971222@outlook.com',
    url='https://github.zlj-zz.com',
    license='MIT',
    package=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    # package_data={
    # '': [ # 方法一：打包数据文件
    # 'themes/*/*/*/*' # 需要按目录层级匹配
    # ]
    # },
    include_package_data=True, # 方法二：配合 MANIFEST.in 文件
    install_requires=[
        'django~=1.11',
    ],
    extras_require={'ipython': ['ipython==6.2.1']},
    scripts=[
        'typeidea/manage.py',
    ],
    entry_points={'console_scripts': [
        'typeidea_manage = manage:main',
    ]},
    classifiers=[ # Optional
        # 软件的成熟度？
        # 3 - Alhpa
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alhpa',

        # 指明项目的受众
        'Intended Audience :: Development',
        'Topic :: Software Development :: Libraries',

        # 选择项目的许可证（License）
        'License :: OSI Approved :: MIT License',

        # 指定项目需要使用的 Python 版本
        'Programming Language :: Python :: 3.7',
    ],
)
